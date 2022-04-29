from random import choice, randint
from turtle import Turtle


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class Car(Turtle):

    X_MAX_POS = 280
    Y_MAX_POS = 250

    def __init__(self):
        super().__init__()
        self.shape('square')
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.color(choice(COLORS))
        self.penup()
        self.goto((randint(-self.X_MAX_POS, self.X_MAX_POS), randint(-self.Y_MAX_POS, self.Y_MAX_POS)))
        self.setheading(180)

    def has_gone(self):
        if self.xcor() > -self.X_MAX_POS:
            return False
        return True

    def reset_position(self):
        self.color(choice(COLORS))
        self.goto((self.X_MAX_POS, randint(-self.Y_MAX_POS, self.Y_MAX_POS)))


class CarManager:

    def __init__(self):
        self.move_distance = STARTING_MOVE_DISTANCE
        self.cars = [Car() for _ in range(randint(10, 20))]

    def move_cars(self):
        for car in self.cars:
            car.forward(self.move_distance)

    def reset_position_cars_manage(self):
        for car in self.cars:
            if car.has_gone():
                car.reset_position()

    def check_collision(self, instance):
        for car in self.cars:
            if car.distance(instance) < 20:
                self.move_distance = 0
                return True
        return False

    def increment_move_distance(self):
        self.move_distance += MOVE_INCREMENT

