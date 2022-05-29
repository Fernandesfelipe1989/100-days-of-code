from random import choice
from turtle import colormode, Screen, Turtle

from utils import COLOURS

SPACE_BETWEEN = 50


def create_columns(obj):
    for _ in range(10):
        obj.color(choice(COLOURS))
        obj.stamp()
        obj.forward(SPACE_BETWEEN)


def turn_right(obj):
    obj.right(90)
    obj.forward(SPACE_BETWEEN)
    obj.right(90)


def turn_left(obj):
    obj.left(90)
    obj.forward(SPACE_BETWEEN)
    obj.left(90)


if __name__ == "__main__":
    jimmy = Turtle()
    colormode(255)
    jimmy.shape('circle')
    jimmy.penup()
    direction = False
    for line in range(10):
        create_columns(jimmy)
        line < 9 and turn_right(jimmy) if direction else turn_left(jimmy)
        direction = not direction
    screen = Screen()
    screen.exitonclick()
