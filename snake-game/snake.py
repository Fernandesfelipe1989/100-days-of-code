from turtle import Turtle


class Snake(Turtle):
    START_POSITION = ((0, 0), (-20, 0), (-40, 0))
    MOVE_DISTANCE = 20
    UP = 90
    DOWN = 270
    RIGHT = 0
    LEFT = 180

    def __init__(self):
        super().__init__()
        self.speed('fastest')
        self.segments = [self.add_segment(position) for position in self.START_POSITION]
        self.head = self.segments[0]

    @staticmethod
    def add_segment(pos):
        instance = Turtle('square')
        instance.color('white')
        instance.penup()
        instance.goto(pos)
        return instance

    def extend(self):
        self.segments.append(self.add_segment(self.segments[-1].position()))

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            position = self.segments[seg_num - 1].position()
            self.segments[seg_num].goto(position)
        self.head.forward(self.MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != self.DOWN:
            self.head.setheading(self.UP)

    def down(self):
        if self.head.heading() != self.UP:
            self.head.setheading(self.DOWN)

    def left(self):
        if self.head.heading() != self.RIGHT:
            self.head.setheading(self.LEFT)

    def right(self):
        if self.head.heading() != self.LEFT:
            self.head.setheading(self.RIGHT)
