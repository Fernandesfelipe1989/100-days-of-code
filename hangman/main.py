from utils import initialize_hangman, stages

USER_CHANGES = len(stages)


def initialize_game(test: bool = False):
    word = 'test'
    if not test:
        word = initialize_hangman()
    word = "teste"
    print(word)
    letter_in_word = []
    secret_letters = []
    for letter in word:
        letter_in_word.append(letter)
        secret_letters.append("_")

    return letter_in_word, secret_letters, secret_letters.count("_")


if __name__ == "__main__":

    letters, secret, left_secret_letters = initialize_game(test=True)
    user_left_life = USER_CHANGES - 1
    used_letters = []

    while "_" in secret and user_left_life > 0:
        print(f"You've choose this letters: {used_letters}" if used_letters else "")
        print(" ".join(secret))
        user_guess = input("Guess a letter: \n").lower()
        used_letters.append(user_guess)
        if user_guess in letters and not(used_letters in secret):
            for index, letter in enumerate(letters):
                if letter == user_guess:
                    secret[index] = letter
        else:
            user_left_life -= 1
            print(f"{stages[user_left_life]}")
    print('The word was:\n', "".join(letters))
    print("You win!" if user_left_life > 0 else "GameOver")





