from SQLdata import SQLData
from twitterAPI import TwitterAPI
from userInterface import UserInterface
from preprocessor import Preprocessor
from textblobSentiment import TextblobSentiment
from naiveBayesSentiment import NaiveBayesSentiment


if __name__ == "__main__":
    # erstellt Datenbank (nur einmalig bei Neuanlage notwendig)
    # sql = SQLData()
    # sql.create_database()

    # fragt Twitter API ab und speichert zurückgelieferte Tweets in der Datenbank
    # api = TwitterAPI()
    # api.download_tweets()

    # bietet User-Kommandos zum Labeln der Tweets
    # ui = UserInterface()
    # ui.greet_user()

    # bereinigt den Textinhalt der Tweets
    # pp = Preprocessor()
    # pp.preprocessing_pipeline()

    # führt Sentimentanalyse mit Textblob durch und erstellt Konfusionsmatrix
    # tb = TextblobSentiment()
    # tb.assign_tb_polarity()
    # tb.get_confusion_matrix()

    # trainiert Naive Bayes-Sentimentklassifikator, führt Kreuzvalidierung durch und
    # gibt Konfusionsmatrix und Evaluationsmaße jedes Folds aus
    nb = NaiveBayesSentiment()
    nb.assign_nb_polarity()
