from time import sleep
from turtle import Screen, Turtle


class Snake:
    START_POSITION = ((0, 0), (-20, 0), (-40, 0))

    def __init__(self):
        self.segments = [self.create_snake_part(position) for position in self.START_POSITION]

    @staticmethod
    def create_snake_part(pos):
        instance = Turtle('square')
        instance.color('white')
        instance.penup()
        instance.goto(pos)
        return instance

    def __len__(self):
        return len(self.segments)


if __name__ == "__main__":
    game_is_on = True
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor('black')
    screen.title("My Snake Game")
    screen.tracer(0)
    snake = Snake()

    while game_is_on:
        screen.update()
        sleep(0.1)
        for seg_num in range(len(snake) - 1, 0, -1):
            position = snake.segments[seg_num - 1].position()
            snake.segments[seg_num].goto(position)
        snake.segments[0].forward(20)
    screen.exitonclick()
