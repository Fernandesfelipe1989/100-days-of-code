import time
from turtle import Screen

from car_manager import CarManager
from player import Player
from scoreboard import Scoreboard

if __name__ == "__main__":
    # Screen Config
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.tracer(0)

    # Create the instance of the game
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

        time.sleep(0.1)
        screen.update()
