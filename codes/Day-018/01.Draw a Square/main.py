from turtle import Turtle, Screen

tuple = Turtle()

for _ in range(4):
    tuple.forward(100)
    tuple.left(90)

screen = Screen()
screen.exitonclick()
