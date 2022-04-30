from turtle import Turtle

from utils import Y


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.read_high_score()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, Y - 10)
        self.font_config = dict(align='center', font=("Arial", 16, "bold"))
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score} ", **self.font_config)

    def read_high_score(self):
        with open('data.txt', 'r') as f:
            high_score = f.read()
        self.high_score = int(high_score) if high_score else self.high_score

    def update_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        self.high_score = self.score if self.score > self.high_score else self.high_score
        self.score = 0
        self.update_scoreboard()
        with open('data.txt', 'w') as file:
            file.write(str(self.high_score))

