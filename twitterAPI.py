import re
import datetime
import tweepy
from tweet import Tweet
from SQLdata import SQLData


class TwitterAPI:
    def __init__(self):
        self.tweets = []
        self.tweet_text = []

    def download_tweets(self):
        # Authentifikation
        consumer_key = "3gNr8ySpbERuZpVuvd7U9Y73p"
        consumer_secret = "PO2W76yFwMlPMt3eIllZjd4QFXsh0BQLx97YTCXkmVDIOx58gl"
        access_token = "1201141846510067714-M68oypMwk2bqSQVILHRmlS5bFXnBrh"
        access_token_secret = "Lo1iObuulmA7ESRZ89oXjoXqXafnUws1HOTkd1S2Vsd0a"
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        api = tweepy.API(auth)

        # auch andere Suchanfragen einbeziehen?
        search_term = "#ExtinctionRebellion"
        quantity_tweets = 500

        #
        self.tweets = tweepy.Cursor(
            api.search, q=search_term, lang="en", tweet_mode="extended", result_type="popular"
        ).items(quantity_tweets)

        sql = SQLData()
        for api_tweet in self.tweets:
            if not api_tweet.full_text.startswith("RT"):
                tweet = Tweet(
                    api_tweet.id,
                    api_tweet.created_at,
                    str(datetime.datetime.now()),
                    str(datetime.datetime.now()),
                    api_tweet.user.screen_name,
                    api_tweet.full_text,
                )
                sql.insert_tweet(tweet)
            else:
                print (f"Tweet mit der ID={api_tweet.id} ist ein Retweet")

