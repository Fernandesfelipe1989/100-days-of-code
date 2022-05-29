from random import choice
from utils import conditions, images_options, options


def print_result_game(first: str, second: str) -> str:
    first_option = f"User choose: \n{images_options.get(first, '')}\n"
    second_option = f"Computer choose: \n{images_options.get(second, '')}\n"
    return first_option + second_option


def choose_winner(user: str, computer: str) -> str:
    result = "Draw"
    condition = conditions.get(user, None)
    if not condition:
        return "Invalid option"
    if condition['win'] == computer:
        result = "You Win"
    if condition['lose'] == computer:
        result = "You lose"
    return result


def play_game(user: str) -> str:
    computer_option = choice(options)
    game_winner = choose_winner(user, computer_option)
    return print_result_game(user, computer_option) + game_winner


if __name__ == "__main__":
    user_option = input("What do you choose? Type rock, paper or scissors\n")
    print(play_game(user_option))
