from turtle import Turtle
from globals import TOP_EDGE, LEFT_EDGE

FONT = ("Courier", 24, "bold")
GAME_OVER_FONT = ("Courier", 35, "bold")


def configure_scoreboard(scoreboard: Turtle):
    scoreboard.hideturtle()
    scoreboard.penup()
    scoreboard.color("white")
    left_offset = LEFT_EDGE + abs(LEFT_EDGE) * 0.05
    top_offset = TOP_EDGE - abs(TOP_EDGE) * 0.17
    scoreboard.goto(left_offset, top_offset)


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        configure_scoreboard(self)
        self.level = 1
        self._update_score()

    def increment_score(self):
        self.level += 1
        self._update_score()

    def _update_score(self):
        self.clear()
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def game_over(self):
        self.home()
        self.write("GAME OVER", align="center", font=GAME_OVER_FONT)
