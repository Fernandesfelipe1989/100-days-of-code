from random import randint
from turtle import Turtle

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
BORDER = 20


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color('blue')
        self.speed('fastest')
        x = SCREEN_WIDTH // 2
        y = SCREEN_HEIGHT // 2
        pos = (randint(-(x-BORDER), x-BORDER), randint(-(y-BORDER), y-BORDER))
        self.goto(pos)


