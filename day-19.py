from turtle import Turtle, Screen
from random import randint
COLOURS = ('red', 'orange', 'yellow', 'green', 'blue', 'purple')


def initialize(height, border):
    turtles = []
    step = (height - border) // len(COLOURS)
    next_y_pos = -(height // 2) + border
    for color in COLOURS:
        turtle = Turtle()
        turtle.shape('turtle')
        turtle.color(color)
        turtle.penup()
        turtle.goto(x=-240, y=next_y_pos)
        next_y_pos += 60
        turtles.append(turtle)
    return turtles


def check_winner(x_finish_pos, racers):
    finish = False
    winner = None
    for racer in racers:
        x = racer.xcor()
        print(x)
        if x >= x_finish_pos:
            finish = True
            winner = racer.color()
            break
    return finish, winner


def race(racers):
    finish = False
    while not finish:
        for _ in range(10):
            move_racers(racers=racers)
        finish, winner = check_winner(x_finish_pos=0, racers=racers)
    print(winner)


def move_racers(racers):
    for racer in racers:
        racer.forward(randint(0, 10))


screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Who's the winner?", prompt="Which turtle will win the race?").lower()
racers = initialize(height=400, border=20)
race(racers=racers)

screen.exitonclick()
