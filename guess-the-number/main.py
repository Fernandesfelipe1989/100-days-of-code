from random import randint
from replit import clear

from utils import LOGO

MAX_NUMBER = 100
MIN_NUMBER = 1

DIFFICULTY = {
    'easy': 10,
    'hard': 5,
}


def initialize() -> int:
    print(LOGO)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100")
    return randint(MIN_NUMBER, MAX_NUMBER)


if __name__ == "__main__":
    run_again = 'yes'
    while run_again == 'yes':
        message = "You've run out of guesses, you lose"
        secret_number = initialize()
        user_guess = False

        difficulty_level = input("Choose a difficulty. Type easy or hard:\n").lower()
        clear()
        user_attempts = DIFFICULTY.get(difficulty_level, 0)
        while user_attempts > 0 and not user_guess:
            print(f"You have {user_attempts} attempts remaining to guess the number")
            guess = int(input("Make a guess:\n"))
            if guess == secret_number:
                user_guess = True
            else:
                user_attempts -= 1
                if guess > secret_number:
                    print("Too high")
                else:
                    print("Too low")
                if user_attempts > 0:
                    print("Guess again")
        if user_guess:
            message = f"You go it! The answer was {secret_number}"
        print(message)
        run_again = input("Do you want to play again? Type yes or no:\n").lower()



