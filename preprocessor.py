import re
import spacy
from SQLdata import SQLData


class Preprocessor:
    def __init__(self):
        self.sql = SQLData()
        # Sprachmodell für Englisch laden
        self.nlp = spacy.load("en_core_web_sm")

    def preprocessing_pipeline(self):
        tweet_list = self.sql.get_all_tweets()
        for tweet in tweet_list:
            tweet_doc = self.nlp(tweet.text)
            clean_tweet = []
            for token in tweet_doc:
                token.lemma_.strip().lower()
                if (
                    token.is_alpha
                    and not token.is_stop
                    and not token.string.startswith("@")
                    and not token.string.startswith("http")
                ):
                    clean_tweet.append(token)
            tweet.clean_text = clean_tweet
            self.sql.update_tweet(tweet)
