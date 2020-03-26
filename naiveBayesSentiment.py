from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from SQLdata import SQLData


class NaiveBayesSentiment:
    def __init__(self):
        self.sql = SQLData()

    def assign_nb_polarity(self):
        tweet_list = self.sql.get_all_tweets()
        X = []
        for tweet in tweet_list:
            X.append(tweet.clean_text)

        y = []
        for tweet in tweet_list:
            y.append(tweet.label)
        # Daten aufteilen für Training und Test (X = Wortliste, y = Label?)
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

        pipe = Pipeline(
            [
                ("bow", CountVectorizer(ngram_range=(1, 1))),
                ("classifier", MultinomialNB()),
            ]
        )

        pipe.fit(X_train, y_train)

        predictions = pipe.predict(X_test)

        print(classification_report(predictions, y_test))
        print("\n")
        print(confusion_matrix(predictions, y_test))
        print(accuracy_score(predictions, y_test))
