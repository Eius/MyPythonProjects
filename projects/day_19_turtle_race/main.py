from turtle import Screen, Turtle
import random

screen = Screen()
screen.setup(width=800, height=600)
screen_width = screen.getcanvas().winfo_width()

is_race_on = False
race_is_over = False
winner = None
turtle_colors = ["red", "green", "blue", "orange", "purple", "yellow"]
racing_turtles = []


def init_turtle_position(turtle_obj, x, y):
    turtle_obj.penup()
    turtle_obj.goto(x=x, y=y)
    turtle_obj.pendown()


def move_forward_randomly(turtle_obj):
    random_distance = random.randint(0, 15)
    turtle_obj.forward(random_distance)


for i in range(0, 6):
    t = Turtle(shape="turtle")
    t.speed(10)
    t.color(turtle_colors[i])
    init_turtle_position(turtle_obj=t, x=-380, y=-100 + i * 50)
    t.speed(5)
    racing_turtles.append(t)

colors_string = ""
for color in turtle_colors:
    s = f"{color}/"
    colors_string +=s
user_bet = screen.textinput(title="Make your bet\n", prompt=f"Which turtle will win the race?\n {colors_string}\n Enter a color: ")

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in racing_turtles:
        move_forward_randomly(turtle)
        if turtle.xcor() >= screen_width/2 - 20:
            is_race_on = False
            race_is_over = True
            winner = turtle
            winner.penup()
            winner.home()
            winner.speed(2)
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
            break

while race_is_over:
    winner.left(180)

screen.exitonclick()