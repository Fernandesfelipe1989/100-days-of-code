from time import sleep
from turtle import Screen, Turtle

INITIAL_SIZE = 3

START_POSITION = ((0, 0), (-20, 0), (-40, 0))


def create_snake_part(position):
    instance = Turtle('square')
    instance.color('white')
    instance.penup()
    instance.goto(position)
    return instance


if __name__ == "__main__":
    game_is_on = True
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor('black')
    screen.title("My Snake Game")
    screen.tracer(0)
    segments = [create_snake_part(position=position) for position in START_POSITION]

    while game_is_on:
        screen.update()
        sleep(0.1)
        for seg_num in range(len(segments) - 1, 0, -1):
            position = segments[seg_num - 1].position()
            segments[seg_num].goto(position)
        segments[0].forward(20)
    screen.exitonclick()
