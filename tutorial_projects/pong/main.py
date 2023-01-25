from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from globals import SCREEN_HEIGHT, SCREEN_WIDTH, L_PADDLE_X_COR, R_PADDLE_X_COR
import time

screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

l_paddle = Paddle((L_PADDLE_X_COR, 0))
r_paddle = Paddle((R_PADDLE_X_COR, 0))
scoreboard = Scoreboard()
ball = Ball(scoreboard)

screen.listen()
screen.onkey(l_paddle.move_up, "w")
screen.onkey(l_paddle.move_down, "s")

screen.onkey(r_paddle.move_up, "Up")
screen.onkey(r_paddle.move_down, "Down")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    ball.detect_collision(l_paddle, r_paddle)

screen.exitonclick()
