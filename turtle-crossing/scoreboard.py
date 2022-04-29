from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color('black')
        self.level = 1
        self.hideturtle()
        self.goto(-200, 250)
        self.penup()
        self.show_level_message()

    def increment_level(self):
        self.level += 1
        self.show_level_message()

    def show_level_message(self):
        self.clear()
        self.write(f"Level: {self.level}", align='center', font=FONT)
