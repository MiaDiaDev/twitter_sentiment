import csv, re
import tweepy
from textblob import TextBlob


class TweetLoader:
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
        quantity_tweets = 300

        #
        self.tweets = tweepy.Cursor(api.search, q=search_term, lang="en").items(
            quantity_tweets
        )

        # Open/create a file to append data to
        csv_file = open("results.csv", "a")

        # Use csv writer
        csv_writer = csv.writer(csv_file)

        i = 0
        for tweet in self.tweets:
            i += 1
            if i >= 50:
                break
            # Append to temp so that we can store in csv later. I use encode UTF-8
            self.tweet_text.append(self.clean_tweet(tweet.text).encode("utf-8"))
            # print (tweet.text.translate(non_bmp_map)) 
            

        # Write to csv and close csv file
        csv_writer.writerow(self.tweet_text)
        csv_file.close()

    def clean_tweet(self, tweet):
        # Remove Links, Special Characters etc from tweet
        return " ".join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())


if __name__ == "__main__":
    sa = TweetLoader()
    sa.download_tweets()
