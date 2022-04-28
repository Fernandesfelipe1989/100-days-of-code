from turtle import Turtle

from utils import BALL_MOVE


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color('white')
        self.shape('circle')
        self.move_speed = 0.1
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.penup()
        self.x_move = BALL_MOVE
        self.y_move = BALL_MOVE

    def move(self):
        x = self.xcor() + self.x_move
        y = self.ycor() + self.y_move
        self.goto(x, y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.move_speed *= 0.9
        self.x_move *= -1

    def detect_collision_paddle(self, instance):
        return self.distance(instance) < 50 and (self.xcor() > 320 or self.xcor() < -320)

    def reset_position(self):
        self.x_move *= -1
        self.y_move *= -1
        self.move_speed = 0.1
        self.goto(0, 0)
