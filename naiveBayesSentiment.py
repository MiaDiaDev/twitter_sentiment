import numpy
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split, KFold
from sklearn.pipeline import Pipeline
from sklearn.metrics import confusion_matrix, classification_report
from SQLdata import SQLData


class NaiveBayesSentiment:
    def __init__(self):
        self.sql = SQLData()

    def assign_nb_polarity(self):
        tweet_list = self.sql.get_all_tweets()
        # Listen mit bereinigtem Textinhalt der Tweets und den manuell vergebenen Labeln erstellen
        text_list = []
        for tweet in tweet_list:
            text_list.append(tweet.clean_text)
        # Liste in ein numpy-Array überführen (als Input für KFold benötigt)
        X = numpy.array(text_list)

        label_list = []
        for tweet in tweet_list:
            label_list.append(tweet.label)
        y = numpy.array(label_list)

        # Anzahl der Partionen festlegen, in die die Datenbasis aufgeteilt werden soll
        kf = KFold(n_splits=10)
        kf.get_n_splits(X)

        run = 0
        # Training des Naive Bayes-Sentimentsklassifikators mit der in der Kreuzvalidierung festgelegten Anzahl an Testläufen
        for train_index, test_index in kf.split(X):
            run += 1
            print("TEST RUN: ", run)
            # Aufteilung in Trainings- und Testdaten
            X_train, X_test = X[train_index], X[test_index]
            y_train, y_test = y[train_index], y[test_index]

            # Pipeline mit Vektorisierung der Daten und Anwendung multinomialen NB-Algorithmus
            pipe = Pipeline(
                [
                    ("bow", CountVectorizer(ngram_range=(1, 1))),
                    ("classifier", MultinomialNB()),
                ]
            )
            # Modell trainieren
            pipe.fit(X_train, y_train)

            predictions = pipe.predict(X_test)
            # Ausgabe der Evaluationsmaße
            print(confusion_matrix(y_test, predictions))
            print(classification_report(y_test, predictions))
