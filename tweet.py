class Tweet:
    def __init__(self, api_id, tweet_date, import_date, update_date, user, text):
        self.api_id = api_id
        self.tweet_date = tweet_date
        self.import_date = import_date
        self.update_date = update_date
        self.user = user
        self.text = text
        self._label = None
        self.tb_polarity = 0
        self.nb_polarity = 0

    #def get_label(self):

        #return self._label

    #def set_label(self, label):

