from random import randint
from replit import clear

from utils import LOGO

DIFFICULTY = {
    'easy': 10,
    'hard': 5,
}

FAIL_MESSAGE = "You've run out of guesses, you lose"
SUCCESSFUL_MESSAGE = "You go it! The answer was {}"

MAX_NUMBER = 100
MIN_NUMBER = 1


def check_answer(attempts, secret):
    if attempts < 1:
        return False
    print(f"You have {attempts} attempts remaining to guess the number")
    guess = int(input("Make a guess:\n"))

    if guess == secret:
        return True

    attempts -= 1
    if guess > secret:
        print("Too high")
    else:
        print("Too low")
    print("Guess again")
    return check_answer(attempts, secret)


def check_message(win, secret):
    return SUCCESSFUL_MESSAGE.format(secret) if win else FAIL_MESSAGE


def initialize() -> int:
    print(LOGO)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100")
    return randint(MIN_NUMBER, MAX_NUMBER)


def game():
    run_again = 'yes'
    while run_again == 'yes':
        secret_number = initialize()
        difficulty_level = input("Choose a difficulty. Type easy or hard:\n").lower()
        clear()
        user_attempts = DIFFICULTY.get(difficulty_level, 0)
        user_guess = check_answer(user_attempts, secret_number)
        print(check_message(user_guess, secret_number))
        run_again = input("Do you want to play again? Type yes or no:\n").lower()


if __name__ == "__main__":
    game()



