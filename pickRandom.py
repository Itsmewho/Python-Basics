import random

word_list = ["ardvark", "baboon","camel"]

chosen_word = random.choice(word_list) # will pick one idx

print(chosen_word)

player_guess = input("Gues a letter: ").lower()

for letter in chosen_word:
    if player_guess == letter:
        print(f"yes the letter '{letter}', is in the word")
    else:
        print("You have lost one life!")

