from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("The python game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()
game_is_on = True

screen.listen()
screen.onkey(snake.move_up, "Up")
screen.onkey(snake.move_left, "Left")
screen.onkey(snake.move_down, "Down")
screen.onkey(snake.move_right, "Right")


while game_is_on:
    time.sleep(0.09)
    screen.update()
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        print("nom nom nom")
        food.refresh()
        snake.extend()
        scoreboard.add_score()

    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset()
        snake.reset()

    # Detect collision with tail
    for segment in snake.snake_segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()

screen.exitonclick()
