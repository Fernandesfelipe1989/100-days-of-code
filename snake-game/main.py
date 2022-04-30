from time import sleep
from turtle import Screen

from food import Food
from snake import Snake
from scoreboard import ScoreBoard
from utils import PRECISION, X, Y

if __name__ == "__main__":
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor('black')
    screen.title("My Snake Game")
    screen.tracer(0)
    snake = Snake()
    food = Food()
    scoreboard = ScoreBoard()
    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")
    game_is_on = True
    while game_is_on:
        screen.update()
        snake.move()
        sleep(0.08)

    # Detect collision with food.
        if snake.head.distance(food) < PRECISION:
            food.refresh()
            scoreboard.update_score()
            snake.extend()

    # Detect collision with wall.
        if snake.head.xcor() > X + PRECISION or snake.head.xcor() < -X - PRECISION \
                or snake.head.ycor() > Y + PRECISION or snake.head.ycor() < - Y - PRECISION:
            scoreboard.reset()
            snake.reset()
            food.refresh()

    # Detect collision with tail
        for segment in snake.segments[1:]:
            if snake.head.position == segment.position:
                scoreboard.reset()
                snake.reset()
                food.refresh()

    screen.exitonclick()
