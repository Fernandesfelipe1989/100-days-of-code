from utils import initialize_hangman

USER_CHANGES = 5


def initialize_game():
    word = initialize_hangman()
    print(word)
    letter_in_word = []
    secret_letters = []
    for letter in word:
        letter_in_word.append(letter)
        secret_letters.append("_")

    return letter_in_word, secret_letters, secret_letters.count("_")


if __name__ == "__main__":
    letters, secret, left_secret_letters = initialize_game()
    user_life = USER_CHANGES

    while left_secret_letters > 0 and user_life > 0:
        print(" ".join(secret))
        user_guess = input("Guess a letter: \n").lower()
        if user_guess in letters and not(user_guess in secret):
            last_count_secret = left_secret_letters
            for index, letter in enumerate(letters):
                if letter == user_guess:
                    secret[index] = letter
            left_secret_letters = secret.count("_")
            print(f"Good job you guess found {last_count_secret - left_secret_letters} letters")
        else:
            print(f"Wrong guess\nYou have remain changes {user_life}")
            user_life -= 1
    print('The word was:\n', "".join(letters))
    print("You win!" if user_life > 0 else "GameOver")





