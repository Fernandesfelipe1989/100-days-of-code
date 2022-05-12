import turtle

import pandas

FONT = ("Courier", 10, "normal")
IMAGE = "blank_states_img.gif"
TITLE = "{}/{} States Correct"


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
    all_states = set(states.state.to_list())
    qty_states = len(all_states)
    screen = turtle.Screen()
    screen.title("U.S. States Game")
    screen.addshape(IMAGE)
    turtle.shape(IMAGE)
    record_guess = set()
    answer_state = True
    while len(record_guess) < qty_states and answer_state != 'Exit':
        answer_state = screen.textinput(
            prompt="What's another state's name?",
            title=TITLE.format(len(record_guess), qty_states)
        )
        answer_state = answer_state and answer_state.title()
        data_state = states[states['state'] == answer_state]
        if not data_state.empty and not (answer_state in record_guess):
            State(name=answer_state, x=data_state.x, y=data_state.y)
            record_guess.add(answer_state)
            qty_right_guess = len(record_guess)

    miss_state = all_states - record_guess
    miss_data = pandas.DataFrame(miss_state)
    miss_data.to_csv("states_to_learn.csv", header=False)
    # turtle.mainloop()
