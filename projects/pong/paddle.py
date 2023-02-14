from turtle import Turtle
from globals import PADDLE_HEIGHT, PADDLE_WIDTH, PADDLE_SPEED


def _configure_paddle(paddle: Turtle, position: tuple):
    paddle.setheading(90)
    paddle.penup()
    paddle.shape("square")
    paddle.color("white")
    y_stretch = PADDLE_HEIGHT / 20
    x_stretch = PADDLE_WIDTH / 20
    paddle.shapesize(stretch_wid=x_stretch, stretch_len=y_stretch)
    paddle.goto(position)


class Paddle(Turtle):

    def __init__(self, position: tuple):
        super().__init__()
        _configure_paddle(self, position)

    def move_up(self):
        if self.ycor() < 240:
            self.forward(PADDLE_SPEED)

    def move_down(self):
        if self.ycor() > -240:
            self.backward(PADDLE_SPEED)
