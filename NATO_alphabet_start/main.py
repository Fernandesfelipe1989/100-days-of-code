import pandas

if __name__ == "__main__":
    nato_data = pandas.read_csv('nato_phonetic_alphabet.csv')
    nato_dictionary = {row.letter.lower(): row.code for _, row in nato_data.iterrows()}
    is_over = False
    while not is_over:
        word = input("Enter a word? \n")
        try:
            result = [nato_dictionary[letter] for letter in word.lower()]
        except KeyError:
            print("Sorry, only letters in the alphabet please")
        else:
            print(result)
            is_over = True


