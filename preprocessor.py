import re
import spacy
from SQLdata import SQLData


class Preprocessor:
    def __init__(self):
        self.sql = SQLData()
        # Sprachmodell für Englisch laden
        self.nlp = spacy.load("en_core_web_sm")

    def preprocessing_pipeline(self, id):
        tweet = self.sql.get_tweet(id)
        tweet_doc = self.nlp(tweet.text)
        clean_tweet = []
        for token in tweet_doc:
            token.lemma_.strip().lower()
            # self.clean_tweet(token.text)
            if (
                not token.is_stop
                and not token.is_punct
                and not token.like_num
                and not token.string.startswith("@")
                and not token.string.startswith("http")
            ):
                clean_tweet.append(token)
        tweet.clean_text = clean_tweet
        self.sql.update_tweet(tweet)
