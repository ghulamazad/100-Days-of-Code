from turtle import Turtle, Screen

turtle = Turtle()

colors = ['dark blue', 'dark green',
          'chocolate', 'gold', 'magenta', 'coral', 'rosy brown']


def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        turtle.forward(100)
        turtle.right(angle)


for shape in range(3, 10):
    turtle.color(colors[shape - 3])
    draw_shape(shape)

screen = Screen()
screen.exitonclick()
