highScore = []
choise = True

highScore.append(int(input("What is the highest score:\n")))

choise = input("Do you want to add more scores (y or n)\n")
if choise == "y":
    while choise == "y":
        highScore.append(int(input("What is the highest score:\n")))
        choise = input("Do you want to add more scores (y or n)\n")

highest_score = 0
for score in highScore:
    if score > highest_score:
        highest_score = score
        
print(highScore)        
print(f"The highest score is: {highest_score}")