from textblob import TextBlob
from SQLdata import SQLData


class TextblobSentiment:
    def __init__(self):
        self.sql = SQLData()

    def assign_tb_polarity(self):
        tweet_list = self.sql.get_all_tweets()
        for tweet in tweet_list:
            analysis = TextBlob(tweet.clean_text)
            tb_polarity = analysis.sentiment.polarity
            tweet.tb_polarity = tb_polarity
            self.sql.update_tweet(tweet)
