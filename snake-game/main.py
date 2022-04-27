from time import sleep
from turtle import Screen

from food import Food
from snake import Snake
from scoreboard import ScoreBoard
from utils import X, Y

if __name__ == "__main__":
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor('black')
    screen.title("My Snake Game")
    screen.tracer(0)
    run_again = "yes"
    while run_again == 'yes':
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
            if snake.head.distance(food) < 15:
                food.refresh()
                scoreboard.update_score()
                snake.extend()

        # Detect collision with wall.
            if snake.head.xcor() > X or snake.head.xcor() < -X or snake.head.ycor() > Y or snake.head.ycor() < - Y:
                game_is_on = False
                scoreboard.game_over()
        screen.reset()
        run_again = screen.textinput(title="Game Over",
                                     prompt=f"Your score: {scoreboard.score}\nDo you want run again: yes or no")
        run_again = run_again and run_again.lower()
    screen.exitonclick()
