import time
from turtle import Screen

from car_manager import CarManager
from player import Player
from scoreboard import Scoreboard

if __name__ == "__main__":

    screen = Screen()
    screen.setup(width=600, height=600)
    screen.tracer(0)
    player = Player()
    scoreboard = Scoreboard()

    screen.listen()
    screen.onkey(fun=player.up, key="Up")

    game_is_on = True
    while game_is_on:
        if player.finish_level():
            scoreboard.increment_level()
        time.sleep(0.1)
        screen.update()
