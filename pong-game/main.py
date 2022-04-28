from random import choice
from time import sleep
from turtle import Screen, Turtle

from paddle import Paddle
from utils import HEIGHT, WIDTH, X


if __name__ == "__main__":
    screen = Screen()
    r_paddle = Paddle(X)
    l_paddle = Paddle(-X)
    screen.tracer(0)
    screen.setup(height=HEIGHT, width=WIDTH)
    screen.bgcolor('black')
    screen.title('The Pong Game')

    screen.listen()
    screen.onkey(fun=r_paddle.go_up, key="Up")
    screen.onkey(fun=r_paddle.go_down, key="Down")
    game_is_on = True
    while game_is_on:
        screen.update()

    screen.exitonclick()
