import random
from random import choice
from turtle import Turtle, Screen, colormode

SHAPES = [
    ('triangle', 3),
    ('square', 4),
    ('pentagon', 5),
    ('hexagon', 6),
    ('heptagon', 7),
    ('octagon', 8),
    ('nonagon', 9),
    ('decagon', 10),
]


class SHAPE:

    def __init__(self, name, number_sides):
        self.name = name
        self.number_sides = number_sides
        self.angle = self.calculate_internal_angle(number_sides)
        self.size = 100

    @staticmethod
    def calculate_internal_angle(number_sides):
        total_angle = (number_sides - 2) * 180
        return 180 - (total_angle // number_sides)

    def __repr__(self):
        return self.name


DRAW_SHAPE = [SHAPE(*shape) for shape in SHAPES]


class Jimmy(Turtle):

    def initialize(self, color, shape):
        self.shape(shape)
        self.color(color)

    def draw_dash_line(self, size, dash_size):
        for _ in range(0, size):
            self.pendown()
            self.forward(dash_size)
            self.penup()
            self.forward(dash_size)

    def draw_square(self, size):
        for _ in range(0, 4):
            self.forward(100)
            self.right(90)

    def draw_shape(self, number_sides, size, angle):
        for _ in range(0, number_sides):
            self.right(angle)
            self.forward(size)

    @staticmethod
    def create_rgb_colour() -> tuple[int]:
        return tuple(random.randint(0, 255) for _ in range(0, 3))

    def create_shapes(self):
        for shape in DRAW_SHAPE:
            self.color(self.create_rgb_colour())
            self.draw_shape(number_sides=shape.number_sides, size=shape.size, angle=shape.angle)

    def create_random_walk(self):
        self.speed(0)
        self.hideturtle()
        self.width(5)
        move_options = [self.forward, self.backward]
        turn_options = [self.right, self.left]

        for _ in range(0, 1000):
            self.color(self.create_rgb_colour())
            move_action = choice(move_options)
            turn_action = choice(turn_options)
            move_action(20)
            turn_action(90)

    def create_spirograph(self, size_gap):
        self.speed(0)
        self.shape('arrow')
        self.width(1)
        for current in range(int(360/size_gap)):
            self.color(self.create_rgb_colour())
            self.circle(100)
            self.setheading(self.heading() + size_gap)


if __name__ == "__main__":
    timmy = Jimmy()
    colormode(255)
    timmy.initialize('black', 'arrow')
    timmy.draw_dash_line(50, 10)
    timmy.reset()
    timmy.create_shapes()
    timmy.reset()
    timmy.create_random_walk()
    timmy.reset()
    timmy.create_spirograph(5)
    screen = Screen()
    screen.exitonclick()
