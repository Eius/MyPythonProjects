import pandas
import random


class DataManager:
    def __init__(self):
        super().__init__()
        self.all_words_csv_path = "data/data.csv"
        self.unknown_words_csv_path = "data/unknown_data.csv"
        self.col_1 = None
        self.col_2 = None
        self.df_list = self.load_all_words_from_csv()

    def load_all_words_from_csv(self):
        with open(self.all_words_csv_path, "r") as csv:
            df = pandas.read_csv(csv)
            self.col_1 = df.columns[0]
            self.col_2 = df.columns[1]
            return df.to_dict(orient="records")

    def pick_random_word(self):
            return random.choice(self.df_list)

    def remove_known_word(self, word):
        self.df_list.remove(word)
        self.save_unknown_words()

    def save_unknown_words(self):
        with open(self.unknown_words_csv_path, "w") as csv:
            df = pandas.DataFrame(self.df_list)
            df.to_csv(self.unknown_words_csv_path, index=False)
