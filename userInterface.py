from SQLdata import SQLData


class UserInterface:
    def __init__(self):
        self.sql = SQLData()

    def greet_user(self):
        command = input("Bitte Befehl eingeben: ")
        if command.startswith("lt"):
            self.label_unlabelled_tweet()
        elif command.startswith("gt"):
            tweet = self.sql.get_tweet(id)
            print(tweet.text)
        elif command.startswith("ul"):
            self.update_label(command)

    def update_label(self, command):
        try:
            split_input = command.split(" ")
            id = split_input[1]
            label = split_input[2]
            tweet = self.sql.get_tweet(id)
            tweet.label = label
            self.sql.update_tweet(tweet)
        except:
            print("Fehler")

    def label_unlabelled_tweet(self):
        try:
            tweet = self.sql.get_next_tweet_without_label()
            print(tweet.text)
            label = input("Bitte Label eingeben: ")
            tweet.label = label
            self.sql.update_tweet(tweet)
        except:
            print("Fehler")

    