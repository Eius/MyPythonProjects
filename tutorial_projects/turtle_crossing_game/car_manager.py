from turtle import Turtle
import random
from globals import LEFT_EDGE, RIGHT_EDGE, TOP_EDGE, BOTTOM_EDGE, CAR_SPAWN_CHANCE, FAST_CAR_CHANCE, \
    CAR_MOVE_INCREMENT, FAST_CAR_MOVE_INCREMENT, CAR_MOVE_SPEED, FAST_CAR_MOVE_SPEED

COLORS = ["white", "red", "pink", "light slate gray", "navy", "firebrick"]
MIN_START_Y = BOTTOM_EDGE + TOP_EDGE * 0.2
MAX_START_Y = TOP_EDGE + BOTTOM_EDGE * 0.2


def configure_car(car: Turtle):
    car.showturtle()
    car.shape("square")
    car.penup()
    car.setheading(180)
    car.speed(1)
    car.shapesize(stretch_wid=1, stretch_len=2)
    car.color(random.choice(COLORS))
    start_y = random.uniform(MIN_START_Y, MAX_START_Y)
    car.goto(RIGHT_EDGE, start_y)


class CarManager:
    def __init__(self):
        self.car_pool = CarPool()
        self.active_cars = []
        self.car_speed = CAR_MOVE_SPEED
        self.fast_car_speed = FAST_CAR_MOVE_SPEED

    def spawn_car(self):
        rand_chance = random.random()
        if rand_chance < CAR_SPAWN_CHANCE:
            car = self.car_pool.new_car()
            configure_car(car)
            self.active_cars.append(car)
            if rand_chance < FAST_CAR_CHANCE:
                car.speed(2)
        print(f"New card spawned. Total active cars: {len(self.active_cars)}")

    def move_cars(self):
        for car in self.active_cars:
            if car.speed() == 1:
                car.forward(self.car_speed)
            else:
                car.forward(self.fast_car_speed)
            if car.xcor() < LEFT_EDGE:
                self.car_pool.deactivate_car(car)
                self.active_cars.remove(car)

    def level_up(self):
        self.car_speed += CAR_MOVE_INCREMENT
        self.fast_car_speed += FAST_CAR_MOVE_INCREMENT


class CarPool:
    def __init__(self):
        self.inactive_cars = []

    def new_car(self):
        if self.inactive_cars:
            car = self.inactive_cars[0]
            self.inactive_cars.remove(car)
            return car

        else:
            return Turtle()

    def deactivate_car(self, car: Turtle):
        car.hideturtle()
        self.inactive_cars.append(car)
