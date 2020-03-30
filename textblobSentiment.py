from textblob import TextBlob
from SQLdata import SQLData


class TextblobSentiment:
    def __init__(self):
        self.sql = SQLData()
        self.prediction = []
        self.labeled = []

    # alle Tweets aus der Datenbank laden und Sentimentanalyse mit Textblob durchführen
    def assign_tb_polarity(self):
        tweet_list = self.sql.get_all_tweets()
        for tweet in tweet_list:
            self.labeled.append(int(tweet.label))
            analysis = TextBlob(tweet.clean_text)
            tb_polarity = analysis.sentiment.polarity
            # Polarität in selbst definierte Label überführen
            if tb_polarity > 0:
                tb_polarity = 1
            elif tb_polarity < 0:
                tb_polarity = 3
            else:
                tb_polarity = 2
            # Attribut TB_Polarity des untersuchten Tweets in der Datenbank updaten
            tweet.tb_polarity = tb_polarity
            self.sql.update_tweet(tweet)

            self.prediction.append(tb_polarity)

    # Konfusionsmatrix der durch TB vergebenen Polaritäten erstellen
    def get_confusion_matrix(self):
        if not len(self.labeled) == len(self.prediction):
            raise Exception("Länge der Listen ist ungleich")

        true_positives = 0
        true_neutrals = 0
        true_negatives = 0
        pos_pred_neut = 0
        pos_pred_neg = 0
        neut_pred_pos = 0
        neut_pred_neg = 0
        neg_pred_pos = 0
        neg_pred_neut = 0

        # Abgleich der beiden Label-Listen
        for i in range(0, len(self.labeled)):
            if self.labeled[i] == 1:
                if self.prediction[i] == 1:
                    true_positives += 1
                elif self.prediction[i] == 2:
                    pos_pred_neut += 1
                elif self.prediction[i] == 3:
                    pos_pred_neg += 1
                else:
                    print("Fehler beim Erstellen der TB Konfusionsmatrix")
            elif self.labeled[i] == 2:
                if self.prediction[i] == 1:
                    neut_pred_pos += 1
                elif self.prediction[i] == 2:
                    true_neutrals += 1
                elif self.prediction[i] == 3:
                    neut_pred_neg += 1
                else:
                    print("Fehler beim Erstellen der TB Konfusionsmatrix")
            elif self.labeled[i] == 3:
                if self.prediction[i] == 1:
                    neg_pred_pos += 1
                elif self.prediction[i] == 2:
                    neg_pred_neut += 1
                elif self.prediction[i] == 3:
                    true_negatives += 1
                else:
                    print("Fehler beim Erstellen der TB Konfusionsmatrix")
            else:
                print("Fehler beim Erstellen der TB Konfusionsmatrix")

        print("          pos.", "neut.", "neg.")
        print("positive: ", true_positives, pos_pred_neut, pos_pred_neg)
        print("neutral:  ", neut_pred_pos, true_neutrals, neut_pred_neg)
        print("negative: ", neg_pred_pos, neg_pred_neut, true_negatives)
