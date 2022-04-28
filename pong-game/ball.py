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

    def move(self, x_move, y_move):
        x = self.ycor() + x_move
        y = self.ycor() + y_move
        self.goto(x, y)

    def bounce(self):
        print('Here')
        print(self.position())
        if self.xcor() + PRECISION > X:
            self.move(x_move=-BALL_MOVE, y_move=BALL_MOVE)
        if self.xcor() - PRECISION > -X:
            self.move(x_move=BALL_MOVE, y_move=BALL_MOVE)
        if self.ycor() + PRECISION > Y:
            self.move(x_move=BALL_MOVE, y_move=-BALL_MOVE)
        if self.ycor() - PRECISION > -Y:
            self.move(x_move=BALL_MOVE, y_move=BALL_MOVE)

    def detect_collision_paddle(self, instance):
        return self.distance(instance) < PRECISION
