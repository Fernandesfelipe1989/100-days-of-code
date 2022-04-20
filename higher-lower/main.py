from random import choices
from replit import clear

from utils import DATA, LOGO, VERSUS

MESSAGE = "{} {}: {}, {}, from {}."


def select_samples(data):
    return choices(data, k=2)


if __name__ == "__main__":
    score = 0
    print(LOGO)
    higher = True
    while higher:
        a, b = select_samples(DATA)

        print(MESSAGE.format('Compare', 'A', a['name'], a['description'], a['country']))
        print(VERSUS)
        print(MESSAGE.format('Against', 'B', b['name'], b['description'], b['country']))
        user_answer = input('Who has more followers? Type A or B:\n').lower()
        user_choice, other_data = (a, b) if user_answer == 'a' else (b, a)
        higher = user_choice.get('follower_count') > other_data.get('follower_count')
        if higher:
            score += 1
            print(f"You're right! Current score: {score}.")
        else:
            print(f"Sorry, that's wrong. Final score: {score}.")
        clear()
