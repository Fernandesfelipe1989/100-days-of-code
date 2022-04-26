from time import sleep
from turtle import Screen, Turtle

from snake import Snake

if __name__ == "__main__":
    game_is_on = True
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor('black')
    screen.title("My Snake Game")
    screen.tracer(0)
    snake = Snake()

    while game_is_on:
        screen.update()
        sleep(0.1)
        snake.move()

    screen.exitonclick()
