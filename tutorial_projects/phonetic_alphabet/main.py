import pandas

df = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter: row.code for (index, row) in df.iterrows()}

user_input = input("What is your name?: ")
processed_words = user_input.replace(" ", "").upper()
processed_letters = [letter for letter in processed_words]
result = [phonetic_dict[letter] for letter in processed_letters]

print(result)
