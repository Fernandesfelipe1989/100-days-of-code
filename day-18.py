from turtle import Turtle, Screen


def calculate_internal_angle(number_sides):
    total_angle = (number_sides - 2)*180
    return 180 - (total_angle % number_sides)


SHAPES = [
    ('triangle', 3, 120, 100),
    ('square',  4, 90, 100),
    ('pentagon',  4, 90, 100),
]


class SHAPE:

    def __init__(self, name, number_sides, angle, size):
        self.name = name
        self.number_sides = number_sides
        self.angle = angle
        self.size = size

    def __repr__(self):
        return self.name


DRAW_SHAPE = [SHAPE(*shape) for shape in SHAPES]


def initialize(color, shape):
    obj = Turtle()
    obj.shape(shape)
    obj.color(color)
    return obj


def draw_dash_line(obj, size, dash_size):
    for _ in range(0, size):
        obj.pendown()
        obj.forward(dash_size)
        obj.penup()
        obj.forward(dash_size)


def draw_square(obj, size):
    for _ in range(0, 4):
        obj.forward(100)
        obj.right(90)


def draw_shape(obj, number_sides, size, angle):
    for _ in range(0, number_sides):
        obj.right(angle)
        obj.forward(size)


timmy = initialize('black', 'arrow')
# draw_square(timmy)
# draw_dash_line(timmy, 50, 5)
# draw_shape(obj=timmy, number_sides=4, size=100, angle=90)
for shape in DRAW_SHAPE:
    draw_shape(obj=timmy, number_sides=shape.number_sides, size=shape.size, angle=shape.angle)


screen = Screen()
screen.exitonclick()
