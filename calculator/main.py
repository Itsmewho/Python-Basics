import os

clear = lambda: os.system("cls")

import sys

sys.path.append("calculator")
from art import logo


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {"+": add, "-": subtract, "*": multiply, "/": divide}


def calc():
    print(logo)

    num1 = float(input("What is the first number?: \n"))
    for symbol in operations:
        print(symbol)
    should_continue = True

    while should_continue != True:
        operation_symbol = input("Pick an operation from the line above: \n")
        num2 = float(input("What is the second number?: \n"))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)
        print(f"{num2} {operation_symbol} {num2} = {answer}")

        if input(f"Type in 'y', to coninue calc with {answer}") == "y":
            num1 = answer
        else:
            should_continue = False
            clear()
            calc()


calc()
