from random import choice
from time import sleep
from turtle import Screen, Turtle


HEIGHT = 600
WIDTH = 800
BORDER = 50
X = (WIDTH - 2 * BORDER) // 2
LEFT = 180
RIGHT = 0
MOVE = 20

POSITIONS = [(X, -50), (X, -30), (X, -10), (X, 10), (X, 30), (X, 50)]


class Paddle(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.shapesize(stretch_wid=5, stretch_len=1)

        self.penup()
        self.goto((X, 0))

    def go_up(self):
        y = self.ycor() + MOVE
        self.goto(self.xcor(), y)

    def go_down(self):
        y = self.ycor() - MOVE
        self.goto(self.xcor(), y)


if __name__ == "__main__":
    screen = Screen()
    paddle = Paddle()
    screen.tracer(0)
    screen.setup(height=HEIGHT, width=WIDTH)
    screen.bgcolor('black')
    screen.title('The Pong Game')

    screen.listen()
    screen.onkey(fun=paddle.go_up, key="Up")
    screen.onkey(fun=paddle.go_down, key="Down")
    game_is_on = True
    while game_is_on:
        screen.update()

    screen.exitonclick()
