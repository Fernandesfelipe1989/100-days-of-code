from turtle import Turtle

from utils import BALL_MOVE, PRECISION, X, Y


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color('white')
        self.shape('circle')
        self.speed(2)
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.penup()

    def move(self):
        x, y = self.bounce(x_move=BALL_MOVE, y_move=BALL_MOVE)
        print(x, y)
        self.goto(x, y)

    def bounce(self, x_move, y_move):
        # x = -x_move if self.xcor() + x_move + PRECISION > X else x_move
        y = -y_move if self.ycor() + y_move + PRECISION > Y else y_move
        return self.xcor() + x_move, self.ycor() + y

    def detect_collision_paddle(self, instance):
        return self.distance(instance) < PRECISION
