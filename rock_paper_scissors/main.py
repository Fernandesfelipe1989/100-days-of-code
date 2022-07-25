from rock_paper_scissors.simulators import RockPaperScissorSimulator

if __name__ == "__main__":
    game = RockPaperScissorSimulator()
    game.get_user_choice()
    print(game.simulator())
