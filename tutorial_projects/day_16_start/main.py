# from turtle import Turtle, Screen
#
# timmy = Turtle()
# my_screen = Screen()
# timmy.shape("turtle")
# timmy.color("green")
# timmy.fd(100)
# my_screen.exitonclick()

from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = "l"

print(table)
