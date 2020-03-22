from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from SQLdata import SQLData


class NaiveBayesSentiment:
    def __init__(self):
        self.sql = SQLData()

    def assign_nb_polarity(self, id):
        tweet = self.sql.get_tweet(id)
