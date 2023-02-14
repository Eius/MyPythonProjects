import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
from globals import SCREEN_WIDTH, SCREEN_HEIGHT

screen = Screen()
screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
screen.title("Turtle Game")
screen.bgcolor("black")
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move_up, "Up")
screen.onkey(player.move_down, "Down")

game_is_on = True
while game_is_on:
    time.sleep(0.05)
    screen.update()
    car_manager.spawn_car()
    car_manager.move_cars()

    # Detect collision with a car
    for car in car_manager.active_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    # Detect win condition
    if player.is_at_finish_line():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.increment_score()

screen.exitonclick()
