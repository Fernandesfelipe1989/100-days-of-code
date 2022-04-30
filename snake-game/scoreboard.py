from turtle import Turtle

from utils import Y


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, Y - 10)
        self.font_config = dict(align='center', font=("Arial", 16, "bold"))
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score} ", **self.font_config)

    def update_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        self.high_score = self.score if self.score > self.high_score else self.high_score
        self.score = 0
        self.update_scoreboard()
        
    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over", **self.font_config)
