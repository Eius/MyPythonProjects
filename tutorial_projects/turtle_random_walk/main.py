import turtle
from turtle import Turtle, Screen
import random

turtle.colormode(255)
t = Turtle()
t.shape("triangle")
t.shapesize(0.5)
t.speed(0)
t.color("royal blue")
t.pensize(8)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


def random_turn():
    rotations = [0, 90, 180, 270]
    t.setheading(random.choice(rotations ))


for _ in range(25000):
    t.color(random_color())
    t.forward(15)
    random_turn()


screen = Screen()
screen.exitonclick()
