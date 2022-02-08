from turtle import Turtle, Screen

etch = Turtle()
screen = Screen()


def move_forwards():
    etch.forward(20)


def move_backwards():
    etch.backward(20)


def turn_left():
    etch.left(10)


def turn_right():
    etch.right(10)


def reset():
    screen.resetscreen()