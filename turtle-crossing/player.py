from turtle import Turtle

STARTING_POSITION = (0, -280)
FINISH_LINE_Y = 280
MOVE_DISTANCE = 10


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.color('black')
        self.penup()

    def up(self):
        self.forward(MOVE_DISTANCE)
