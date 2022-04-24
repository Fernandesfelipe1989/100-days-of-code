from random import choice
from turtle import colormode, Screen, Turtle

from utils import COLOURS


def create_columns(obj, direction):
    move_direction = obj.forward if direction else obj.backward
    for _ in range(10):
        obj.color(choice(COLOURS))
        obj.stamp()
        move_direction(25)


def turn_right(obj):
    obj.right(90)
    obj.forward(25)
    obj.left(90)


def turn_left(obj):
    obj.left(90)
    obj.forward(25)
    obj.right(90)


if __name__ == "__main__":
    jimmy = Turtle()
    colormode(255)
    jimmy.shape('circle')
    jimmy.penup()
    direction = False
    for line in range(10):
        create_columns(jimmy, direction)
        if direction:
            turn_right(jimmy)
            direction = False
        else:
            turn_left(jimmy)
            direction = True
    screen = Screen()
    screen.exitonclick()
