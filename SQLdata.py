import sqlite3
import datetime
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
        # prüft, ob schon ein Tweet mit der selben ID vorhanden ist
        if self._tweet_exists(tweet):
            print("Eintrag existiert bereits")
            return
        # Werte in eine Zeile schreiben
        try:
            self.cursor.execute(f"INSERT INTO Tweets VALUES ({tweet.api_id},'{tweet.tweet_date}','{tweet.import_date}','{tweet.update_date}','{tweet.user}','{tweet.text}','{tweet.label}',{tweet.tb_polarity},{tweet.nb_polarity})")
            self.connect.commit()
        except:
            print (f"Fehler bei Tweet mit der ID={tweet.api_id}")
             

    def get_tweet(self, tweet):
        if self._tweet_exists(tweet):
            rows = self.cursor.execute(f"SELECT * FROM Tweets WHERE ID={tweet.api_id}")
            results = []
            for row in rows:
                results.append(row)
            row = results[0]
            tweet = self._cast_row_to_tweet(row)
            return tweet
        else:
            print ("Kein Tweet gefunden")

    def _tweet_exists(self, tweet):
        rows = self.cursor.execute(f"SELECT * FROM Tweets WHERE ID={tweet.api_id}")
        results = []
        for row in rows:
            results.append(row)

        if not results:
            return False
        else:
            return True

    def update_tweet(self, tweet):
        # prüft, ob Eintrag bereits existiert
        if not self.get_tweet(tweet.api_id):
            print("Eintrag existiert nicht")
            return
        self.cursor.execute(
            f"UPDATE Tweets SET UPDATE_DATE='{datetime.datetime.now()}', TEXT='{tweet.text}', LABEL='{tweet.label}', TB_POLARITY={tweet.tb_polarity}, NB_POLARITY={tweet.nb_polarity} WHERE ID={tweet.api_id}"
        )
        self.connect.commit()

    def delete_tweet(self, id):
        # prüft, ob Eintrag bereits existiert
        if not self.get_tweet(id):
            print("Eintrag existiert nicht")
            return
        self.cursor.execute(f"DELETE FROM Tweets WHERE ID={id}")
        self.connect.commit()

    def _cast_row_to_tweet(self, row):
        tweet = Tweet(row[0], row[1], row[2], row[3], row[4], row[5])
        tweet.label = row[6]
        tweet.tb_polarity = row[7]
        tweet.nb_polarity = row[8]
        return tweet
