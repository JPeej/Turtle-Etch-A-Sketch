import commands
from turtle import Turtle, Screen

etch = Turtle()
screen = Screen()

screen.listen()
screen.onkey(fun=commands.move_forwards, key="w")
screen.onkey(fun=commands.move_backwards, key="s")
screen.onkey(fun=commands.turn_left, key="a")
screen.onkey(fun=commands.turn_right, key="d")
screen.onkey(fun=commands.reset, key="c")
screen.exitonclick()