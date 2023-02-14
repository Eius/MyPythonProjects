import turtle
from turtle import Turtle, Screen
import random

t = Turtle()
t.shape("turtle")
t.color("royal blue")
t.pensize(5)

n_sides = 3

def random_hex():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = "#{:02x}{:02x}{:02x}".format(r, g, b)
    return color

for _ in range(8):
    t.pencolor(random_hex())
    for _ in range(n_sides):
        t.forward(100)
        t.right(360/n_sides)
    n_sides += 1

screen = Screen()
screen.exitonclick()
