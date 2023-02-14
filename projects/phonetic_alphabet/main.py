import pandas

df = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter: row.code for (index, row) in df.iterrows()}

def generate_phonetic():
    user_input = input("Enter a word: ")
    try:
        processed_words = user_input.replace(" ", "").upper()
        processed_letters = [letter for letter in processed_words]
        phonetic_words = [phonetic_dict[letter] for letter in processed_letters]
        result = " | ".join(phonetic_words)
        print(result)

    except KeyError:
        print("Sorry, only letter in the english alphabet please.")


while True:
    try:
        generate_phonetic()

    except KeyboardInterrupt:
        print("\nTerminating program...")
        break



