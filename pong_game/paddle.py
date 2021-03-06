from turtle import Turtle

from utils import PADDLE_MOVE


class Paddle(Turtle):

    def __init__(self, x):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.speed("fastest")
        self.penup()
        self.goto((x, 0))

    def go_up(self):
        y = self.ycor() + PADDLE_MOVE
        self.goto(self.xcor(), y)

    def go_down(self):
        y = self.ycor() - PADDLE_MOVE
        self.goto(self.xcor(), y)
