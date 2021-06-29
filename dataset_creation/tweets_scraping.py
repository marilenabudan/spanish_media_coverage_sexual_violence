import GetOldTweets3 as got
from datetime import date
import pandas as pd
import os

'''
tweets_scraping.py
* Python code that scrapes [NUM_DIRS + MAX_TWEETS] tweets from each Twitter account in the list of strings 'ACCOUNTS'
* and stores them in directories of MAX_TWEETS in the DATA_PATH specified.

* Arguments
* * Does not read the arguments, all variables aiming to be changed, have to be modified in the global variables
* * of the script.
* Requirements
* * libraries: GetOldTweets3, datetime, pandas and os
'''

# GLOBAL VARIABLES
ACCOUNTS = ["el_pais", "elmundoes", "20m", "eldiario", "A3Noticias", "elconfidencial", "okdiario", "LaVanguardia",
            "sextaNoticias", "informativost5", "rtve", "abc_es", "elperiodico", "La_SER", "larazon_es"]

DATA_PATH = "../data/tweets/"
NUM_DIRS = 10
MAX_TWEETS = 1000

def get_tweets(account, until_date, max_tweets=MAX_TWEETS):
    '''
    Given a Twitter account and a date, scrape max_tweets backwards starting from
    until_date.
    Return a pandas DataFrame with max_tweets.
    '''
    if not until_date:
        until_date = date.today().strftime("%Y-%m-%d")

    tweetCriteria = got.manager.TweetCriteria().setUsername(account).setMaxTweets(max_tweets).setUntil(until_date)
    tweets = got.manager.TweetManager.getTweets(tweetCriteria)

    tweets_list = [
        [t.id, t.permalink, t.username, t.to, t.text, t.date, t.retweets, t.favorites, t.mentions, t.hashtags, t.geo]
        for t in tweets]

    tweets_df = pd.DataFrame(tweets_list)
    tweets_df.columns = ["id", "permalink", "username", "to", "text", "date", "retweets", "favorites", "mentions",
                         "hashtags", "geo"]
    return tweets_df

if __name__ == "__main__":
    last_date = dict(zip(ACCOUNTS, [None] * len(ACCOUNTS)))

    for directory in range(1, NUM_DIRS + 1):
        # Check the directory exists, else create it
        dir_path = os.path.abspath(f'''{DATA_PATH}{directory}''')
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)

        time_interval_df = pd.DataFrame(columns=['account', 'start', 'end'])

        # For each Twitter account
        for account in ACCOUNTS:
            # Scrape tweets
            df = get_tweets(account, last_date[account])
            # Store them in a csv file
            filename = f'''{dir_path}/{account}.csv'''
            df.to_csv(filename, index=False, header=True)
            # Update last_date
            last_date[account] = df['date'].max()[:10]

            # Store the interval of time for each account in the current directory
            time_interval_df.append({'account': account,
                                     'start': df['date'].min()[:10],
                                     'end': df['date'].max()[:10]},
                                    ignore_index=True)

        time_interval_df.to_csv(f'''{dir_path}/__Interval.csv''', index=False)
