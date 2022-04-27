from turtle import Screen, Turtle
HEIGHT = 600
WIDTH = 800


if __name__ == "__main__":
    screen = Screen()
    screen.setup(height=HEIGHT, width=WIDTH)
    screen.bgcolor('black')
    screen.title('The Pong Game')
    screen.listen()
    
    screen.exitonclick()
