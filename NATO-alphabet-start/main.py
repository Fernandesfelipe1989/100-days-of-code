import pandas

if __name__ == "__main__":
    nato_data = pandas.read_csv('nato_phonetic_alphabet.csv')
    nato_dictionary = {row.letter: row.code for _, row in nato_data.iterrows()}
    word = input("Word? \n")
    word = word and word.upper()
    result = [nato_dictionary.get(letter) for letter in word if nato_dictionary.get(letter)]
    print(result)


