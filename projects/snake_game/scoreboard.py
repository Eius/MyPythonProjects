from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 16, "bold")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.speed(0)
        self.goto(0, 270)
        self.score = 0
        with open("high_score.txt", "r") as file:
            self.high_score = int(file.read())
        self._update_scoreboard()

    def add_score(self):
        self.score += 1
        self._update_scoreboard()

    def _update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} | High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("high_score.txt", "w") as file:
                file.write(f"{self.high_score}")
        self.score = 0
        self._update_scoreboard()
