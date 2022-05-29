from turtle import Screen, Turtle

timmy = Turtle()
timmy.shape("turtle")
timmy.color('blue')
for i in range(0, 10):
    timmy.forward(100)
    timmy.left(45.0)
    timmy.forward(100)
    timmy.right(-45.0)
    timmy.forward(100)

my_screen = Screen()

my_screen.exitonclick()
