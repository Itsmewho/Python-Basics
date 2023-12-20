import random

print("Welcome to head or tails")

player = input("Please choose heads or tails: \n")
if player == "tails":
    player == 1
if player == "heads":
    player = 2
elif player == "":
    print("you got to make a choise")


headOrtails = random.randint(1, 2)

if headOrtails == 1:
    print("you got tails")
else:
    print("You got head")
