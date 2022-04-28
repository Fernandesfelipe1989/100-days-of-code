from turtle import Turtle

from utils import Y


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, Y - 20)
        self.font_config = dict(align='center', font=("Arial", 16, "bold"))
        self.write_scoreboard()

    def write_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.l_score} | Score: {self.r_score}", **self.font_config)

    def add_left_score(self):
        self.l_score += 1
        self.write_scoreboard()

    def add_right_score(self):
        self.r_score += 1
        self.write_scoreboard()
