from turtle import Turtle, Screen


def initialize(color, shape):
    obj = Turtle()
    obj.shape(shape)
    obj.color(color)
    return obj


def draw_dash_line(obj, size, dash_size):
    for _ in range(0, size):
        obj.color('black')
        obj.forward(dash_size)
        obj.color('white')
        obj.forward(dash_size)


def draw_square(obj):
    for _ in range(0, 4):
        obj.forward(100)
        obj.right(90)


timmy = initialize('black', 'arrow')
# draw_square(timmy)
draw_dash_line(timmy, 50, 5)


screen = Screen()
screen.exitonclick()
