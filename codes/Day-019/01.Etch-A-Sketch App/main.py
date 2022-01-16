import turtle as t

turtle = t.Turtle()


def move_forward():
    turtle.forward(10)


def move_backward():
    turtle.backward(10)


def counter_clockwise():
    turtle.setheading(turtle.heading()+10)


def clockwise():
    turtle.setheading(turtle.heading()-10)


def clear_draw():
    turtle.clear()
    turtle.penup()
    turtle.home()
    turtle.pendown()


screen = t.Screen()
screen.listen()
screen.onkey(key='w', fun=move_forward)
screen.onkey(key='s', fun=move_backward)
screen.onkey(key='a', fun=counter_clockwise)
screen.onkey(key='d', fun=clockwise)
screen.onkey(key='c', fun=clear_draw)
screen.exitonclick()
