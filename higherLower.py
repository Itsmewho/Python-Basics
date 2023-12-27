import random

import os

clear = lambda: os.system("cls")

my_list = random.randrange(1, 101)
gues = []
lives = 0


print("Welcome to the number guessing game!")
print("I'am thinking about a number between 1 and 100")
print("Can you guess the right number?")
print(my_list)

while True:
    difficulty = input("Do you want to play easy of hard? (Type in e or h)")
    if difficulty.startswith("e"):
        lives = 10
        break
    if difficulty.startswith("h"):
        lives = 5
        break
    else:
        clear()

if lives == 10:
    clear()
    print(f"You have chosen the easy route and got '{lives}', guesses!")
elif lives == 5:
    clear()
    print(f"You are a hard ass! you got '{lives}', lives!")

while gues != my_list and lives != 0:
    gues = int(input("What is the number?\n"))
    lives -= 1
    clear()
    print(f"Wrong number! you guessed {gues}")
    if lives == 0:
        clear()
        print("Game's over you lose!")
    if gues == my_list:
        clear()
        print("You won!")
