import turtle
from turtle import Turtle, Screen
import random

t = Turtle()
turtle.colormode(255)
t.color("royal blue")
t.speed(0)
t.pensize(2)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        t.pencolor(random_color())
        t.circle(100)
        t.right(size_of_gap)

draw_spirograph(20)

screen = Screen()
screen.exitonclick()