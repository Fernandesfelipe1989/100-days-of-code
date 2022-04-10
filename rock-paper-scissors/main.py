from random import choice

options = ('rock', 'paper', 'scissors')
conditions = {
    'paper': {
        'win': 'rock',
        'lose': 'scissors',
    },
    'rock': {
        'win': 'scissors',
        'lose': 'paper',
    },
    'scissors': {
        'win': 'paper',
        'lose': 'rock',
    }
}
images_options = {
    'paper': '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''',
    'rock':  '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''',
    'scissors': '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''',
}


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
