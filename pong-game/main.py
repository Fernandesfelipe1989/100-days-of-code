from random import choice
from time import sleep
from turtle import Screen, Turtle

from ball import Ball
from paddle import Paddle
from utils import HEIGHT, WIDTH, PRECISION, PADDLE_MOVE, X, Y


if __name__ == "__main__":
    screen = Screen()
    r_paddle = Paddle(X)
    l_paddle = Paddle(-X)
    ball = Ball()
    screen.tracer(0)
    screen.setup(height=HEIGHT, width=WIDTH)
    screen.bgcolor('black')
    screen.title('The Pong Game')

    screen.listen()
    screen.onkey(fun=r_paddle.go_up, key="Up")
    screen.onkey(fun=r_paddle.go_down, key="Down")
    screen.onkey(fun=l_paddle.go_up, key="w")
    screen.onkey(fun=l_paddle.go_down, key="s")
    game_is_on = True
    while game_is_on:
        sleep(0.1)
        screen.update()
        ball.move()

        # Detect collision with wall
        (ball.ycor() + PRECISION > Y or ball.ycor() - PRECISION < -Y) and ball.bounce()

        # Detect collision with paddle
        ball.detect_collision_paddle(r_paddle) and ball.bounce_paddle()
        ball.detect_collision_paddle(l_paddle) and ball.bounce_paddle()


    screen.exitonclick()
