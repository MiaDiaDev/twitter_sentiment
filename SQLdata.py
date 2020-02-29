import sqlite3
from tweet import Tweet


class SQLData:
    def __init__(self):
        database_name = "tweets_db.db"
        self.connect = sqlite3.connect(database_name)
        self.cursor = self.connect.cursor()

    def create_database(self):
        self.cursor.execute(
        """CREATE TABLE Tweets(
        ID INT PRIMARY KEY     NOT NULL,
        TWEET_DATE     TEXT    NOT NULL,
        IMPORT_DATE    TEXT    NOT NULL,
        UPDATE_DATE    TEXT    NOT NULL,
        USER           TEXT    NOT NULL,
        TEXT           TEXT    NOT NULL,
        LABEL          TEXT,
        TB_POLARITY    INT,
        NB_POLARITY    INT
        );"""
        )
    
    def insert_tweet(self, tweet):
        if self.get_tweet(tweet.id):
            return
        self.cursor.execute(f"INSERT INTO Tweets VALUES ({tweet.api_id},'{tweet.tweet_date}','{tweet.import_date}','{tweet.update_date}','{tweet.user}','{tweet.text}','{tweet.label}',{tweet.tb_polarity},{tweet.nb_polarity})")
        self.connect.commit()

    def get_tweet(self, id):
        rows = self.cursor.execute(f"SELECT * FROM Tweets WHERE ID={id}")
        if not rows:
            print(f"Keinen Tweet mit dieser ID={id} gefunden")
            return None

        row = rows[0]
        tweet = self.cast_row_to_tweet(row)
        return tweet

    def cast_row_to_tweet(self, row):
        tweet = Tweet(row[0],row[1],row[2],row[3],row[4],row[5])
        tweet.label = row[6]
        tweet.tb_polarity = row[7]
        tweet.nb_polarity = row[8]
        return tweet