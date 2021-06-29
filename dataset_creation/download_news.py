# IMPORTS
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from bs4 import BeautifulSoup
from pathlib import Path
import regex as re
import argparse
import random
import time
import os

from dataset_creation.utilities import utils

# ENV. VARIABLES
GOOGLE_CHROMEDRIVER_PATH = '/resources/ChromeDriver/chromedriver_googleChrome'
TWEETS_PATH = '../data/tweets/'
NEWS_PATH = '../data/news/'

def store_news(path, media, tweet_id, soup):
    try:
        news_author, news_provider, news_creation_datetime, news_uri, \
        news_title, news_headline, news_guid, news_article = utils.extract_information(path, media, tweet_id, soup)

        utils.write_newsml(path, media, tweet_id, news_author, news_provider, news_creation_datetime, news_uri, \
                           news_title, news_headline, news_guid, news_article)

        return True
    except:
        print('Error with url {}'.format(news_url))
        return False


def get_link_from_twitter(driver, news_url):
    driver.get(news_url)
    html_string = re.sub("/ Twitter", '', driver.page_source)
    soup = BeautifulSoup(html_string, 'html.parser')
    title = soup.find('title').get_text()
    print(title)

    title = re.sub('"', '', title)
    return re.search("(?P<url>https?://[^\s]+)", title).group("url")


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("-media", "-m", nargs='*', help="Input the name of the media to download or write 'all' for considering all files.")
    parser.add_argument("-directories", "-dir", nargs='*', help="Input directories.")
    args = parser.parse_args()

    media_list = args.media
    directories = args.directories

    if not directories:
        print("You need to input at least one directory with the flag -directories or -dir")
        exit(0)
    if not media_list:
        print("Since no media has been specified, all files of the directories inputed will be considered")

    if not media_list or media_list[0] == 'ALL':
        media_list = ['20m', 'A3Noticias', 'abc_es', 'elconfidencial', 'elmundoes', 'elperiodico', 'informativost5', 'La_SER', 'larazon_es',\
                 'LaVanguardia', 'okdiario', 'rtve', 'sextaNoticias']

    # Set up the web driver
    options = Options()
    options.headless = True
    options.add_argument("--window-size=1920,1200")

    driver_path = os.path.abspath(GOOGLE_CHROMEDRIVER_PATH)
    driver = webdriver.Chrome(options=options, executable_path=driver_path)

    try:
        with open('problematic_tweetids.txt', 'r') as file:
            problematic_tweetids = [line[:-1].strip("'") for line in file.readlines()]
        file.close()
    except:
        problematic_tweetids = []


    # FOR ONE MEDIA AND MULTIPLE DIRECTORIES
    for directory in directories:
        print("\n\n\n*** Processing directory", directory)
        # Obtain tweets classified as sexual assault
        orig_path = os.path.abspath(TWEETS_PATH+"{}".format(directory))
        dest_path = os.path.abspath(NEWS_PATH+"{}".format(directory))
        for media in media_list:
            print("\n** Processing media", media)
            ids_url_dict = utils.get_links_media(media, orig_path)
            if ids_url_dict:
                ids_downloaded = []
                Path(dest_path).mkdir(parents=True, exist_ok=True) #Check if the output directory exists, else create it
                # Discard tweets already downloaded
                for file in os.listdir(dest_path):
                    if media in file: ids_downloaded.append(file.split(':')[-1].replace('.xml', ''))

                print(" --- Tweets downloaded", ids_downloaded)
                # Collect news corresponding to those tweets
                for tweet_id, news_url in ids_url_dict.items():
                    if str(tweet_id) not in ids_downloaded and str(tweet_id) not in problematic_tweetids:
                        try:
                            if news_url[:15] == "https://twitter":
                                print(" --- Accessing true link of", tweet_id)
                                news_url = utils.obtain_nofollow_links(news_url)
                                if news_url == None:
                                    problematic_tweetids.append(str(tweet_id))
                                    continue
                            print(" --- Downloading", tweet_id)
                            time.sleep(random.uniform(5, 20))  # random waits
                            driver.get(news_url)
                            soup = BeautifulSoup(driver.page_source, features='lxml')
                            succeeded = store_news(dest_path, media, tweet_id, soup)
                        except:
                            succeeded = False

                        if succeeded is False and str(tweet_id) not in problematic_tweetids:
                            problematic_tweetids.append(str(tweet_id))

                with open('problematic_tweetids.txt', 'w') as file:
                    file.writelines("%s\n" % tid for tid in problematic_tweetids)
                file.close()

    driver.close()