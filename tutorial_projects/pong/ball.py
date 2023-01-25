from turtle import Turtle
from scoreboard import Scoreboard
from globals import BALL_SPEED, BALL_SIZE, TOP_EDGE, BOTTOM_EDGE, R_PADDLE_X_COR, L_PADDLE_X_COR, BALL_COLOR, \
    LEFT_EDGE, RIGHT_EDGE


def _configure_ball(ball: Turtle):
    ball.speed(0)
    ball.setheading(90)
    ball.penup()
    ball.shape("circle")
    ball.color(BALL_COLOR)
    y_stretch = BALL_SIZE / 20
    x_stretch = BALL_SIZE / 20
    ball.shapesize(stretch_wid=x_stretch, stretch_len=y_stretch)


class Ball(Turtle):
    def __init__(self, scoreboard: Scoreboard):
        super().__init__()
        _configure_ball(self)
        self.x_move = 10
        self.y_move = 10
        self.scoreboard_ref = scoreboard
        self.move_speed = BALL_SPEED

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def detect_collision(self, l_paddle: Turtle, r_paddle: Turtle):

        # Detect collision with wall
        if self.ycor() > TOP_EDGE - BALL_SIZE / 2 or self.ycor() < BOTTOM_EDGE + BALL_SIZE / 2:
            self._bounce_y()

        # Detect collision with paddle
        if self.distance(r_paddle) < 60 and self.xcor() > R_PADDLE_X_COR - 20 or \
                self.distance(l_paddle) < 60 and self.xcor() < L_PADDLE_X_COR + 20:
            self._bounce_x()

        # Detect if right paddle scored
        if self.xcor() < LEFT_EDGE:
            self._reset_position()
            self.scoreboard_ref.l_point()

        # Detect if left paddle scored
        elif self.xcor() > RIGHT_EDGE:
            self._reset_position()
            self.scoreboard_ref.r_point()

    def _bounce_y(self):
        self.y_move *= -1

    def _bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def _reset_position(self):
        self.home()
        self.move_speed = BALL_SPEED
        self._bounce_x()

