from random import choice

INPUT = 'palavras.txt'
words = []


def initialize_hangman():
    with open(INPUT, 'r') as input_document:
        for word in input_document:
            words.append(word)
    return choice(words)


if __name__ == "__main__":
    print(initialize_hangman())
