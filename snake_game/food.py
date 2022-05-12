from random import randint
from turtle import Turtle

from utils import PRECISION, X, Y


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color('blue')
        self.speed('fastest')

    def refresh(self):
        pos = (randint(-X + PRECISION, X - PRECISION), randint(-Y + PRECISION, Y - PRECISION))
        self.goto(pos)
