import csv
import re
from textblob import TextBlob
from twitterAPI import TwitterAPI
from SQLdata import SQLData


if __name__ == "__main__":
    sql = SQLData()
    #sql.create_database()
    sa = TwitterAPI()
    sa.download_tweets()
