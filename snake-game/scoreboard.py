from turtle import Turtle

from utils import Y


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, Y - 10)
        self.font_config = dict(align='center', font=("Arial", 16, "bold"))
        self._show_score()

    def _show_score(self):
        self.write(f"Score: {self.score}", **self.font_config)

    def update_score(self):
        self.score += 1
        self.clear()
        self._show_score()
        
    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over", **self.font_config)
