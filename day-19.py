from turtle import Turtle, Screen
from random import randint

COLOURS = ('red', 'orange', 'yellow', 'green', 'blue', 'purple')


def initialize(height, border):
    turtles = []
    step = (height - 2*border) // len(COLOURS)
    print(step)
    next_y_pos = -(height // 2) + border
    for color in COLOURS:
        print(next_y_pos)
        turtle = Turtle()
        turtle.shape('turtle')
        turtle.color(color)
        turtle.penup()
        turtle.goto(x=-240, y=next_y_pos)
        next_y_pos += step
        turtles.append(turtle)
    return turtles


def check_winner(x_finish_pos, racers):
    finish = False
    winner = None
    for racer in racers:
        x = racer.xcor()
        if x >= x_finish_pos:
            finish = True
            winner = racer
            break
    return finish, winner


def race(racers):
    finish = False
    while not finish:
        move_racers(racers=racers)
        finish, winner = check_winner(x_finish_pos=150, racers=racers)
    return winner


def move_racers(racers):
    for racer in racers:
        racer.forward(randint(0, 10))


screen = Screen()
screen.title("Welcome to the turtle race!")
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Who's the winner?", prompt="Which turtle will win the race?").lower()
racers = initialize(height=400, border=20)
winner = race(racers=racers)
winner.write(f"I won the race")
screen.textinput(prompt="Congratulations your bet is right" if winner.color()[0].lower() == user_bet
                 else "Sorry your bet is wrong", title="Race Result")

screen.exitonclick()
