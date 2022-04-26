from turtle import Turtle


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

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            position = self.segments[seg_num - 1].position()
            self.segments[seg_num].goto(position)
        self.segments[0].forward(20)
