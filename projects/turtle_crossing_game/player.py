from turtle import Turtle
from globals import BOTTOM_EDGE, TOP_EDGE

STARTING_POSITION = (0, BOTTOM_EDGE + TOP_EDGE * 0.12)
MOVE_DISTANCE = 10
FINISH_LINE_Y = TOP_EDGE - 20


def configure_player(player: Turtle):
    player.shape("turtle")
    player.color("green")
    player.penup()
    player.setheading(90)


class Player(Turtle):
    def __init__(self):
        super().__init__()
        configure_player(self)
        self.go_to_start()

    def move_up(self):
        self.forward(20)

    def move_down(self):
        self.backward(20)

    def go_to_start(self):
        self.goto(STARTING_POSITION)

    def is_at_finish_line(self):
        return self.ycor() > TOP_EDGE + BOTTOM_EDGE * 0.04
