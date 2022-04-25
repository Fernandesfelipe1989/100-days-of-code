from turtle import Turtle, Screen
from random import randint
SUCCESSFUL_MESSAGE = "Congratulations your bet is right"
FAIL_MESSAGE = "Sorry your bet is wrong"
PLAY_AGAIN_MESSAGE = "Click Ok to play again or write stop"

class Race:
    COLOURS = ('red', 'orange', 'yellow', 'green', 'blue', 'purple')

    def __init__(self, border):
        height = 400
        width = 500
        self.racers = []
        self.winner = None
        self.x_finish_pos = width - 150
        step = (height - 2 * border) // len(self.COLOURS)
        print(step)
        next_y_pos = -(height // 2) + border
        for color in self.COLOURS:
            print(next_y_pos)
            turtle = Turtle()
            turtle.shape('turtle')
            turtle.color(color)
            turtle.penup()
            turtle.goto(x=-240, y=next_y_pos)
            next_y_pos += step
            self.racers.append(turtle)

    def check_winner(self):
        finish = False
        for racer in self.racers:
            x = racer.xcor()
            if x >= self.x_finish_pos:
                finish = True
                racer.write(f"I won the race")
                self.winner = racer
                break
        return finish

    def start_race(self):
        finish = False
        while not finish:
            self.move_racers()
            finish = self.check_winner()
        return finish and self.winner

    def move_racers(self):
        for racer in self.racers:
            racer.forward(randint(0, 10))


screen = Screen()
screen.title("Welcome to the turtle race!")
finish = False
while not finish:
    user_bet = screen.textinput(title="Who's the winner?", prompt="Which turtle will win the race?").lower()
    racer = Race(border=20)
    winner = racer.start_race()
    message = SUCCESSFUL_MESSAGE if winner.color()[0].lower() == user_bet else FAIL_MESSAGE
    message = "\n".join([message, PLAY_AGAIN_MESSAGE])
    user_answer = screen.textinput(prompt=message, title="Race Result").lower()
    finish = user_answer == 'stop'
    screen.clear()
screen.exitonclick()
