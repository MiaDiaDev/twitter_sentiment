import re
import spacy
from SQLdata import SQLData


class Preprocessor:
    def __init__(self):
        self.sql = SQLData()
        # Sprachmodell für Englisch laden
        self.nlp = spacy.load("en_core_web_sm")

    def preprocessing_pipeline(self):
        # alle Tweets aus der Datenbank laden und in für spaCy interpretierbare Doc-Objekte überführen
        tweet_list = self.sql.get_all_tweets()
        for tweet in tweet_list:
            tweet_doc = self.nlp(tweet.text)
            clean_tweet = []
            # Tokenisierung, Lemmatiiserung und Kleinschreibung
            for token in tweet_doc:
                token.lemma_.strip().lower()
                # Entfernung von Zahlen, Symbolen, Stoppwörtern, Mentions und Links
                if (
                    token.is_alpha
                    and not token.is_stop
                    and not token.string.startswith("@")
                    and not token.string.startswith("http")
                ):
                    clean_tweet.append(token)
            # bereinigten Textinhalt des Tweets als neues Attribut in der Datenbank ablegen
            tweet.clean_text = clean_tweet
            self.sql.update_tweet(tweet)
