import turtle as t
import random


color_list = [(72, 204, 98), (118, 15, 133), (114, 151, 207), (183, 115, 128), (122, 69, 97),  (14, 77, 62), (195, 197, 42), (12, 62, 54), (87, 133, 255), (79, 78, 210), (21, 201, 155), (46, 150, 56), (219, 45, 33), (239, 168, 146), (24, 169, 101),
              (245, 71, 21), (49, 243, 165), (187, 4, 48), (2, 56, 112), (225, 22, 49), (178, 18, 164), (181, 193, 63), (144, 165, 214), (126, 121, 167), (30, 85, 9), (120, 20, 173), (62, 8, 181), (128, 15, 121), (113, 133, 104), (7, 187, 124)]

t.colormode(255)
turtle = t.Turtle()
turtle.speed('fastest')
turtle.penup()
turtle.hideturtle()
turtle.setheading(225)
turtle.forward(300)
turtle.setheading(0)
numbers_of_dots = 100

for dot_count in range(1, numbers_of_dots+1):
    turtle.dot(20, random.choice(color_list))
    turtle.forward(50)

    if dot_count % 10 == 0:
        turtle.setheading(90)
        turtle.forward(50)
        turtle.setheading(180)
        turtle.forward(500)
        turtle.setheading(0)


screen = t.Screen()
screen.exitonclick()
