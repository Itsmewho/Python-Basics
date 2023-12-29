import random
import os

clear = lambda: os.system("cls")


game = False
number = random.randrange(1, 11)
gues = []
lives = 0


print("Do you want to play Higer or Lower?")
while True:
    choice = input("Type in yes or no: ")
    if choice.startswith("y"):
        clear()
        break
    if choice.startswith("n"):
        game = True
        clear()
        print("Good bye!")
        break


while game != True:
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

while game !=True and gues != lives and number:
    gues = int(input("Whats is your number? \n"))
    lives -= 1
    clear()
    print(f"Wrong number! you guessed {gues}")
    if lives == 0:
        game = True
        clear()
        print("Game's over you lose!")
    if gues == number:
        game = True
        clear()
        print("You won!")
