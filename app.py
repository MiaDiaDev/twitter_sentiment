from twitterAPI import TwitterAPI
from SQLdata import SQLData
from userInterface import UserInterface
from preprocessor import Preprocessor
from textblobSentiment import TextblobSentiment
from naiveBayesSentiment import NaiveBayesSentiment


if __name__ == "__main__":
    sql = SQLData()
    # sql.create_database()
    # api = TwitterAPI()
    # api.download_tweets()

    # test = sql.get_tweet(1233796208503795712)
    # print(test.text)
    # sql.delete_tweet(1236252642759847936)

    # ui = UserInterface()
    # ui.greet_user()

    # pp = Preprocessor()
    # pp.preprocessing_pipeline()

    # tb = TextblobSentiment()
    # tb.assign_tb_polarity()

    nb = NaiveBayesSentiment()
    nb.assign_nb_polarity()
