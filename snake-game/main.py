from turtle import Screen, Turtle

INITIAL_SIZE = 3


def move_forward():
    print("Here")
    snake.forward(20)


if __name__ == "__main__":
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor('black')
    screen.title("My Snake Game")
    snake = Turtle()
    snake.penup()
    snake.shape('square')
    snake.color('white')
    snake.turtlesize(stretch_len=INITIAL_SIZE, stretch_wid=1)


    screen.exitonclick()
