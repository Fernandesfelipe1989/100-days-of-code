from random import choice
from utils import images_options


class RockPaperScissorSimulator:
    OPTIONS = ('rock', 'paper', 'scissors')
    CONDITIONS = {
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

    def __init__(self):
        self.user_choice = None
        self.computer_choice = None

    def get_user_choice(self):
        user_option = input(f"What do you choose? Type {self.show_the_game_options()}\n")
        self.user_choice = user_option

    def show_the_game_options(self) -> str:
        return ", ".join([f'{option}' for option in self.OPTIONS])

    def result_game(self) -> str:
        first_option = f"User choose: \n{images_options.get(self.user_choice, '')}\n"
        second_option = f"Computer choose: \n{images_options.get(self.computer_choice, '')}\n"
        return first_option + second_option

    def choose_winner(self) -> str:
        self.computer_choice = choice(self.OPTIONS)
        condition = self.CONDITIONS.get(self.user_choice, None)
        return self.conditions_to_win(condition)

    def conditions_to_win(self, condition):
        result = "Draw"
        if not condition:
            return "Invalid option"
        if condition['win'] == self.computer_choice:
            result = "You Win"
        if condition['lose'] == self.computer_choice:
            result = "You lose"
        return result

    def simulator(self) -> str:
        game_winner = self.choose_winner()
        return self.result_game() + game_winner
