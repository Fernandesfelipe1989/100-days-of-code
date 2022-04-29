import time
from turtle import Screen

from car_manager import CarManager
from player import Player
from scoreboard import Scoreboard

if __name__ == "__main__":
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.tracer(0)

    game_is_on = True
    while game_is_on:
        time.sleep(0.1)
        screen.update()
