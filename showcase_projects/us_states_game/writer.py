from turtle import Turtle

FONT = ("Arial", 9, "bold")

class Writer(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()

    def write_state(self, x, y, state_name):
        self.goto((x, y))
        self.write(state_name, align="center", font=FONT)
