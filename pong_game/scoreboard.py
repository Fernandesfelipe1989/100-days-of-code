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
        self.goto(0, Y - 100)
        self.font_config = dict(align='center', font=("Courier", 80, "normal"))
        self.write_scoreboard()

    def write_scoreboard(self):
        self.clear()
        self.write(f"{self.l_score}  |  {self.r_score}", **self.font_config)

    def left_point(self):
        self.l_score += 1
        self.write_scoreboard()

    def right_point(self):
        self.r_score += 1
        self.write_scoreboard()
