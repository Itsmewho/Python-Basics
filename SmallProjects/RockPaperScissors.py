import random
import time
import os

clear = lambda: os.system("cls")


ai_choice = ["rock", "paper", "scissor"]

player_score = 0
computer_score = 0

game_over = False


print("Best of 3!")
print("Let's play, rock, paper, scissors")

time.sleep(0.5)

player = input("What's your name? : ").title()

while game_over != True:
    computer_choice = random.choice(ai_choice)       
    
    response = input("What do you choose? : rock, paper or scissors?").lower()
    if response.startswith("r"):
        player_choice = "rock"
        clear()
    if response.startswith("p"):
        player_choice = "paper"
        clear()
    if response.startswith("s"):
        player_choice = "scissors"
        clear()
    if response.startswith("q"):
        game_over = True
        print("Goodbye!")
        time.sleep(1)
        clear()
    

    print(f"Computer has: {computer_choice}")
    print(f"{player.title()} has: {player_choice}")

    if computer_choice == player_choice:
        print("its a draw!")
    elif (
        (computer_choice == "rock" and player_choice == "scissor")
        or (computer_choice == "scissor" and player_choice == "paper")
        or (computer_choice == "paper" and player_choice == "rock")
    ):
        print("Computer wins")
        computer_score += 1
    elif (
        (player_choice == "rock" and computer_choice == "scissor")
        or (player_choice == "scissor" and computer_choice == "paper")
        or (player_choice == "paper" and computer_choice == "rock")
    ):
        print(f"{player.title()} wins")
        player_score += 1

    print(f"Computer score = {computer_score} and player score = {player_score}")

    if (computer_score == 2 and player_score == 0) or (computer_score == 2 and player_score == 1):
        game_over = True
        print("Computer wins")
    elif (player_score == 2 and computer_score == 0) or (player_score == 2 and computer_score == 1):
        game_over = True
        print(f"{player} wins!")