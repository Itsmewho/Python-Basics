import time
import os

clear = lambda: os.system("cls")
import sys

sys.path.append("CoffeeMachine")

from menu import menu
from resources import resources


profit = 0
coffee_machine = False
continue_program = False


def if_resource_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Srry there is not enough {item}")
            return False
    return True


def process_coins():
    print("Pleace insert coins")
    total = int(input("How many quaters: ")) * 0.25
    total += int(input("How many dimes: ")) * 0.10
    total += int(input("How many nickels: ")) * 0.05
    total += int(input("How many pennys: ")) * 0.01
    return total


def is_transaction(money, drink_cost):
    if money >= drink_cost:
        change = round(money - drink_cost, 2)
        print(f"Here is ${change} change")
        global profit
        profit += drink_cost
        return True
    else:
        print("There is not enough money. Money is refunded.")
        return False


def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}☕️. Enjoy")


while coffee_machine != True:
    choice = input("What would you like? (espresso/latte/cappuccino)")
    if choice == "off":
        coffee_machine = True
        print("The coffee machine is turning off")
        time.sleep(1)
        clear()
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}gr")
        print(f"Money: ${profit}")
    else:
        drink = menu[choice]
        if if_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])
