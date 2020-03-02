import csv
import re
from textblob import TextBlob
from twitterAPI import TwitterAPI
from SQLdata import SQLData


if __name__ == "__main__":
    sql = SQLData()
    #sql.create_database()
    #sa = TwitterAPI()
    #sa.download_tweets()
    
    test = sql.get_tweet(1233796208503795712)
    print(test.text)
    sql.delete_tweet(1233796156309823489)