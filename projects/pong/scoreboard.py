from turtle import Turtle
from globals import TOP_EDGE

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-120, TOP_EDGE - 90)
        self.write(self.l_score, align="center", font=("Courier", 60, "bold"))
        self.goto(120, TOP_EDGE - 90)
        self.write(self.r_score, align="center", font=("Courier", 60, "bold"))

    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()
