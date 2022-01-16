import turtle as t
import random


directions = [0, 90, 180, 270]

turtle = t.Turtle()
t.colormode(255)
turtle.pensize(15)
turtle.speed('fastest')


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


for _ in range(200):
    turtle.color(random_color())
    turtle.forward(30)
    turtle.setheading(random.choice(directions))

screen = t.Screen()
screen.exitonclick()
