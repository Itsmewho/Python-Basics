

import math
import os
clear = lambda: os.system("cls")

print("Welcome to the fibonacci checker!")

game = False


first_numbers = 20
fib_num1 = 0
fib_num2 = 1
next_number = fib_num2
count = 1

while count <= first_numbers:
    print(next_number, end=" ")

    count += 1
    fib_num1, fib_num2 = fib_num2, next_number
    next_number = fib_num1 + fib_num2

print("\nThat's some shit!")

#Thanks geekforgeeks!

def if_is_square(x):
    sqr = int(math.sqrt(x))
    return sqr * sqr == x

def fibonacci(n):
    return if_is_square(5*n*n + 4) or if_is_square(5*n*n -4)


while game !=True:
    number = int(input("Now give me a number to check if it is a fibonacci: "))
    clear()
    if number == (fibonacci == True):
        print(f"{number} Is a Fibonacci Number")
    else:
        print(f"{number} is not a Fibonacci Number")
    while True:
        print("Do you want to check again?\n")
        response = input("Type in: yes or no: ")
        if response.startswith("y"):
            clear()
            break
        if response.startswith("n"):
            game = True
            clear()
            print("Good bye!")
            break
