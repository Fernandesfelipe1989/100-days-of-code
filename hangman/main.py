from replit import clear

from utils import initialize_hangman, LOGO, STAGES

USER_CHANGES = len(STAGES)


def initialize_game(test: bool = False):
    word = 'test'
    if not test:
        word = initialize_hangman()
    letter_in_word = []
    secret_letters = []
    for letter in word:
        letter_in_word.append(letter)
        secret_letters.append("_")

    return letter_in_word, secret_letters, secret_letters.count("_")


if __name__ == "__main__":

    letters, secret, left_secret_letters = initialize_game(test=False)
    user_left_life = USER_CHANGES - 1
    used_letters = []
    print(LOGO)

    while "_" in secret and user_left_life > 0:
        print(f"You've choose this letters: {used_letters}" if used_letters else "")

        user_guess = input("\nGuess a letter: \n").lower()

        clear()

        if user_guess in used_letters:
            print(f"You've already guessed {user_guess}")
        else:
            used_letters.append(user_guess)
            if user_guess in letters and not(used_letters in secret):
                for index, letter in enumerate(letters):
                    if letter == user_guess:
                        secret[index] = letter

            else:
                print(f"You guessed {user_guess}, that's not in the word. You lose a life.")
                user_left_life -= 1
                print(f"{STAGES[user_left_life]}")
            print(" ".join(secret))
    print(f'The word was: {"".join(letters)}')
    print("You win!" if user_left_life > 0 else "GameOver")





