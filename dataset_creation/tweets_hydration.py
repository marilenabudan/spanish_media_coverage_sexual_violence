import configparser
import pandas as pd
import jsonlines
import tweepy
import os

'''
tweets_hydration.py
* Reads csv files with a summary of the tweets, collect their tweet_ids, hydrate those tweet_ids with the library
* tweepy and store the extended tweets in jsonline format (one json file for each accounts).

* Arguments
* * Does not read the arguments, all variables aiming to be changed, have to be modified in the global variables
* * of the script.
* Requirements
* * Twitter developer credentials stored in a file named config.ini
* * libraries: configparser, pandas, jsonlines, tweepy, sys and os
* Considerations
* * if the DATA_PATH account contains directories or files others than the directories with tweets summary in csv file,
* * specify them in the global variable TO_AVOID.
'''

# GLOBAL VARIABLES
DATA_PATH = "../data/tweets"
ACCOUNTS = ["el_pais", "elmundoes", "20m", "eldiario", "A3Noticias", "elconfidencial", "okdiario", "LaVanguardia",
            "sextaNoticias", "informativost5", "rtve", "abc_es", "elperiodico", "La_SER", "larazon_es"]
TO_AVOID = []

if __name__ == "__main__":
    # Read Twitter developer credentials
    config = configparser.ConfigParser()
    config.read("utilities/config.ini")
    credentials = config["CREDENTIALS"]

    # Access token and consumer information
    consumer_key = credentials["consumer_key"]
    consumer_secret = credentials["consumer_secret"]

    access_key = credentials["access_key"]
    access_secret = credentials["access_secret"]

    # Authenticate credentials
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True)

    # HYDRATION
    for directory in os.listdir(os.path.abspath(DATA_PATH)):
        if directory in TO_AVOID:
            continue

        for account in ACCOUNTS:
            # Obtain tweet_ids
            filename = os.path.abspath(f'''{DATA_PATH}{directory}/{account}.csv''')
            df = pd.read_csv(filename)
            tweet_ids = df["id"]

            # Obtain extended json for each tweet
            extended_tweets = []
            # Get tweets by id
            for t_id in tweet_ids:
                try:
                    stat = api.get_status(t_id, tweet_mode="Extended")
                    extended_tweets.append(stat)

                except tweepy.TweepError as e:
                    try:
                        if ("89" in e.args[0][0]):
                            print(f'''Check your credentials\nError: {e}''')
                        elif ("144" in str(e.args[0][0]["code"])):
                            print(f'''Error hydrating the tweet with id: {t_id}''')
                    except:
                        print(f'''Error: {e}''')

            # Store tweets as json lines
            output_dir = os.path.abspath(f'''{DATA_PATH}{directory}/extended_json''')
            output_path = os.path.abspath(f'''{output_dir}/{account}.json''')
            if not os.path.exists(output_dir):
                os.makedirs(output_dir)
            with jsonlines.open(output_path, 'w') as writer:
                writer.write_all([t._json for t in extended_tweets])
