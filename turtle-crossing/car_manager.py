from random import choice, randint
from turtle import Turtle


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.move_distance = STARTING_MOVE_DISTANCE
        self.cars = [Car() for _ in range(randint(5, 20))]

    def move_cars(self):
        for car in self.cars:
            car.forward(self.move_distance)


class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.color(choice(COLORS))
        self.penup()
        self.goto(randint(-250, 250), randint(-250, 250))
        self.setheading(180)

