from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    X_LEVEL_POSITION = -200
    Y_LEVEL_POSITION = 250

    def __init__(self):
        super().__init__()
        self.color('black')
        self.level = 1
        self.hideturtle()
        self.goto(self.X_LEVEL_POSITION, self.Y_LEVEL_POSITION)
        self.penup()
        self.show_level_message()

    def increment_level(self):
        self.level += 1
        self.show_level_message()

    def show_level_message(self):
        self.clear()
        self.write(f"Level: {self.level}", align='center', font=FONT)

    def reset_level(self):
        self.goto(0, 0)
        self.write(f"Game Over", align='center', font=FONT)


