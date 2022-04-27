from random import randint
from turtle import Turtle

from utils import X, Y


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color('blue')
        self.speed('fastest')

    def refresh(self):
        pos = (randint(-X, X), randint(-Y, Y))
        self.goto(pos)
