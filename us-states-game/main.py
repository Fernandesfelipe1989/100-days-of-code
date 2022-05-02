import turtle

import pandas

IMAGE = "blank_states_img.gif"

FONT = ("Courier", 12, "normal")


class State(turtle.Turtle):

    def __init__(self, name, x, y):
        super().__init__()
        self.color('black')
        self.penup()
        self.hideturtle()
        self.goto(int(x), int(y))
        self.write(name, align='center', font=FONT)


if __name__ == "__main__":
    states = pandas.read_csv("50_states.csv")
    print(states)
    screen = turtle.Screen()
    screen.title("U.S. States Game")
    screen.addshape(IMAGE)
    turtle.shape(IMAGE)
    answer_state = screen.textinput(prompt="What's another state's name?", title="Guess the State")
    answer_state = answer_state and answer_state.title()
    data_state = states[states['state'] == answer_state]

    not data_state.empty and State(name=answer_state, x=data_state.x, y=data_state.y)
    turtle.mainloop()
