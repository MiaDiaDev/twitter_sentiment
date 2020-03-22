from textblob import TextBlob
from SQLdata import SQLData


class TextblobSentiment:
    def __init__(self):
        self.sql = SQLData()

    def assign_tb_polarity(self, id):
        tweet = self.sql.get_tweet(id)
        analysis = TextBlob(tweet.text)
        tb_polarity = analysis.sentiment.polarity
        tweet.tb_polarity = tb_polarity
        self.sql.update_tweet(tweet)
