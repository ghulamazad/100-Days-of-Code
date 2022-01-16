# This code run on Reeborg's World
def turn_right():
    turn_left()
    turn_left()
    turn_left()


def right_move():
    turn_right()
    move()


def left_move():
    turn_left()
    move()


def jump():
    move()
    left_move()
    right_move()
    right_move()
    turn_left()


for i in range(6):
    jump()
