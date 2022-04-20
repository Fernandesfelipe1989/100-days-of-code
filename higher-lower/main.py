from random import sample
from replit import clear

from utils import DATA, LOGO, VERSUS

MESSAGE = "{} {}: {}, a {}, from {}."


def choice_higher(first, second, score):
    if first.get('follower_count') < second.get('follower_count'):
        return False, score
    score += 1
    print(f"You're right! Current score: {score}.")
    return True, score


def compare_user_choice(answer, first, second):
    if answer != 'a':
        second, first = first, second
    return first, second


def game(is_correct, score):
    if not is_correct:
        clear()
        return f"Sorry, that's wrong. Final score: {score}."

    a, b = select_samples(DATA)
    print(MESSAGE.format('Compare', 'A', a['name'], a['description'].lower(), a['country']))
    print(VERSUS)
    print(MESSAGE.format('Against', 'B', b['name'], b['description'].lower(), b['country']))
    user_answer = input('Who has more followers? Type A or B:\n').lower()
    user_choice, other_data = compare_user_choice(user_answer, a, b)
    return game(*choice_higher(user_choice, other_data, score))


def select_samples(data):
    return sample(data, k=2)


if __name__ == "__main__":
    run_again = 'yes'
    while run_again == 'yes':
        print(LOGO)
        print(game(True, 0))

        run_again = input("Do you like to play again: Type yes or no\n").lower()
