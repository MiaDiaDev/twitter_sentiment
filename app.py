import sys, tweepy, csv, re
from textblob import TextBlob


class SentimentAnalysis:
    def __init__(self):
        self.tweets = []
        self.tweetText = []

    def DownloadData(self):
        # authenticating
        consumerKey = "3gNr8ySpbERuZpVuvd7U9Y73p"
        consumerSecret = "PO2W76yFwMlPMt3eIllZjd4QFXsh0BQLx97YTCXkmVDIOx58gl"
        accessToken = "1201141846510067714-M68oypMwk2bqSQVILHRmlS5bFXnBrh"
        accessTokenSecret = "Lo1iObuulmA7ESRZ89oXjoXqXafnUws1HOTkd1S2Vsd0a"
        auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
        auth.set_access_token(accessToken, accessTokenSecret)
        api = tweepy.API(auth)

        # input for term to be searched and how many tweets to search
        searchTerm = input("Enter Keyword/Tag to search about: ")
        NoOfTerms = int(input("Enter how many tweets to search: "))

        # searching for tweets
        self.tweets = tweepy.Cursor(api.search, q=searchTerm, lang="en").items(
            NoOfTerms
        )

        # Open/create a file to append data to
        csvFile = open("result.csv", "a")

        # Use csv writer
        csvWriter = csv.writer(csvFile)

        i = 0
        for tweet in self.tweets:
            i += 1
            if i >= 50:
                break
            # Append to temp so that we can store in csv later. I use encode UTF-8
            self.tweetText.append(self.cleanTweet(tweet.text).encode("utf-8"))
            # print (tweet.text.translate(non_bmp_map))    #print tweet's text
            analysis = TextBlob(tweet.text)

        # Write to csv and close csv file
        csvWriter.writerow(self.tweetText)
        csvFile.close()

    def cleanTweet(self, tweet):
        # Remove Links, Special Characters etc from tweet
        return " ".join(
            re.sub(
                "(@[A-Za-z0-9]+)|([^0-9A-Za-z \t]) | (\w +:\ / \ / \S +)", " ", tweet
            ).split()
        )


if __name__ == "__main__":
    sa = SentimentAnalysis()
    sa.DownloadData()
