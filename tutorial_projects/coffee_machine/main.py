import time

# --- DATA --- #
DRINKS = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit = 0

resources = {
    # Values are in milliliters and grams
    "water": 2500,
    "milk": 1000,
    "coffee": 300,
}
# --- END OF DATA --- #

# --- FUNCTIONS --- #


def is_resource_sufficient(order_ingredients):
    """Returns True when order can be made, False if ingredients are insufficient."""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def process_coins():
    """Return the total calculated from coins inserted."""
    print("Please insert coins.")
    total = int(input("How many 10 cent coins?: ")) * 0.1
    total += int(input("How many 20 cent coins?: ")) * 0.2
    total += int(input("How many 50 cent coins?: ")) * 0.5
    total += int(input("How many 1 euro coins?: "))
    total += int(input("How many 2 euro coins?: ")) * 2
    return total


def is_transaction_successful(money_received, drink_cost):
    """Return True when payment is accepted, or False if money is insufficient."""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        if change > 0:
            print(f"Here is {change}€ in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    for i in range(5, 0, -1):  # Coffee making countdown
        print(f"\rTime remaining: {i} seconds", end='\033[K')
        time.sleep(1)
    print(f"\rHere is your {drink_name} ☕. Enjoy! \n", end='\033[K')

# --- END OF FUNCTIONS --- #


is_on = True

while is_on:
    try:
        choice = input("What would you like? (espresso/latte/cappuccino): ")

        if choice == "off":
            is_on = False

        elif choice == "report":
            print(f"Water: {resources['water']}ml")
            print(f"Milk: {resources['milk']}ml")
            print(f"Coffee: {resources['coffee']}g")
            print(f"Money: {profit}€")
        else:
            drink = DRINKS[choice]
            if is_resource_sufficient(drink["ingredients"]):
                print(f"Cost: {drink['cost']}€")
                payment = process_coins()
                if is_transaction_successful(payment, drink["cost"]):
                    make_coffee(choice, drink["ingredients"])

    except KeyError:
        print("\033[31mInvalid option. Please try again \033[m")
        continue
    except KeyboardInterrupt:
        print("\nExiting program...")
        break
