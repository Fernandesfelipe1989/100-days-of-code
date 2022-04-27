from time import sleep
from turtle import Screen

from food import Food
from snake import Snake
from scoreboard import ScoreBoard

if __name__ == "__main__":
    game_is_on = True
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor('black')
    screen.title("My Snake Game")
    screen.tracer(0)
    screen.listen()
    snake = Snake()
    food = Food()
    scoreboard = ScoreBoard()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")

    while game_is_on:
        screen.update()
        snake.move()
        sleep(0.08)

        if snake.head.distance(food) < 15:
            food.refresh()
            scoreboard.update_score()
    screen.exitonclick()
