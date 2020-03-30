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
        # Authentifikation bei der Twitter API
        consumer_key = "3gNr8ySpbERuZpVuvd7U9Y73p"
        consumer_secret = "PO2W76yFwMlPMt3eIllZjd4QFXsh0BQLx97YTCXkmVDIOx58gl"
        access_token = "1201141846510067714-M68oypMwk2bqSQVILHRmlS5bFXnBrh"
        access_token_secret = "Lo1iObuulmA7ESRZ89oXjoXqXafnUws1HOTkd1S2Vsd0a"
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        api = tweepy.API(auth)

        # Festlegen des Suchbegriffs und der Größe der Rückgabemenge
        search_term = "#ExtinctionRebellion"
        quantity_tweets = 100

        # Definition der Suchparameter
        self.tweets = tweepy.Cursor(
            api.search, q=search_term, lang="en", tweet_mode="extended"
        ).items(quantity_tweets)

        # Speichern der erhaltenen Tweets und ihrer Attribute in der Datenbank
        sql = SQLData()
        for api_tweet in self.tweets:
            # wenn Textinhalt mit "RT" beginnt diesen Tweet nicht speichern
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
                print(f"Tweet mit der ID={api_tweet.id} ist ein Retweet")
