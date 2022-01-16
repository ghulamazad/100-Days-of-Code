from turtle import Turtle, Screen

turtle = Turtle()
for _ in range(50):
    turtle.forward(10)
    turtle.penup()
    turtle.forward(10)
    turtle.pendown()

screen = Screen()
screen.exitonclick()
