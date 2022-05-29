from turtle import Turtle, Screen
from random import randint

MESSAGE = "Which turtle will win the race?"
SUCCESSFUL_MESSAGE = "Congratulations your bet is right"
FAIL_MESSAGE = "Sorry your bet is wrong"
PLAY_AGAIN_MESSAGE = "Which turtle will win the race? Or write stop to exit the game"


class Race:
    COLOURS = ('red', 'orange', 'yellow', 'green', 'blue', 'purple')

    def __init__(self, border):
        height = 400
        width = 500
        self.racers = []
        self.winner = None
        self.x_finish_pos = width - 150
        step = (height - 2 * border) // len(self.COLOURS)
        next_y_pos = -(height // 2) + border
        for color in self.COLOURS:
            turtle = Turtle()
            turtle.shape('turtle')
            turtle.color(color)
            turtle.penup()
            turtle.goto(x=-240, y=next_y_pos)
            next_y_pos += step
            self.racers.append(turtle)

    def check_winner(self):
        has_a_winner = False
        for _racer in self.racers:
            x = _racer.xcor()
            if x >= self.x_finish_pos:
                has_a_winner = True
                _racer.write(f"I won the race")
                self.winner = _racer
                break
        return has_a_winner

    def start_race(self):
        finish = False
        while not finish:
            self.move_racers()
            finish = self.check_winner()
        return finish and self.winner

    def move_racers(self):
        for _racer in self.racers:
            _racer.forward(randint(0, 10))


if __name__ == "__main__":
    screen = Screen()
    screen.title("Welcome to the turtle race!")
    finish_game = False
    user_bet = screen.textinput(title="Who's the winner?", prompt="Which turtle will win the race?").lower()
    while not finish_game:
        racer = Race(border=20)
        winner = racer.start_race()
        message = SUCCESSFUL_MESSAGE if winner.color()[0].lower() == user_bet else FAIL_MESSAGE
        message = "\n".join([message, PLAY_AGAIN_MESSAGE])
        user_bet = screen.textinput(prompt=message, title="Race Result").lower()
        finish_game = user_bet == 'stop'
        screen.clear()
    screen.exitonclick()
