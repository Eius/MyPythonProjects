from coffee_maker import CoffeeMaker
from menu import Menu
from money_machine import MoneyMachine

coffeeMaker = CoffeeMaker()
menu = Menu()
moneyMachine = MoneyMachine()

while True:
    try:
        options = menu.get_items()
        choice = input(f"What would you like? ({options}): ")
        if choice == "off":
            break

        if choice == "report":
            coffeeMaker.report()
            moneyMachine.report()

        else:
            drink = menu.find_drink(choice)
            if drink is not None and coffeeMaker.is_resource_sufficient(drink) and moneyMachine.make_payment(drink.cost):
                coffeeMaker.make_coffee(drink)
            else:
                continue
    except ValueError:
        print("Invalid value. Please try again")
    except KeyboardInterrupt:
        print("\nExiting program...")
        break
