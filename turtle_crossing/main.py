import time
from turtle import Screen

from car_manager import CarManager
from player import Player
from scoreboard import Scoreboard

if __name__ == "__main__":
    # Screen Config
    screen = Screen()
    screen.setup(width=600, height=600)
    play_again = 'yes'
    # Create the instance of the game
    while play_again == "yes":
        screen.tracer(0)
        player = Player()
        scoreboard = Scoreboard()
        car_manager = CarManager()

        # Control Config
        screen.listen()
        screen.onkey(fun=player.up, key="Up")

        game_is_on = True

        while game_is_on:
            # Control the cars flow
            car_manager.move_cars()
            car_manager.reset_position_cars_manage()

            # Check if the player win the level
            if player.finish_level():
                scoreboard.increment_level()
                car_manager.increment_move_distance()

            # Check if was a collision
            if car_manager.check_collision(player):
                scoreboard.reset_level()
                game_is_on = False

            time.sleep(0.1)
            screen.update()
        play_again = screen.textinput(prompt='Do you want play again? Yes or No', title="Game over")
        play_again = play_again and play_again.lower()
        screen.clearscreen()
screen.exitonclick()
