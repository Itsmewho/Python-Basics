import random
import sys
sys.path.append("Hangman")

from words import word_list 
from art import stages, logo

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
chosen_word = random.choice(word_list)
lives = 6

print(logo)
print("")
print("Welcome let's play a game!")
print("")


display_word = []

word_length = len(chosen_word)
for _ in range(word_length):
    display_word += "_"

print (display_word)
print("")

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in display_word:
        lives == lives
        print(f"You've already have: {guess}")

    for posistion in range(word_length):
        letter = chosen_word[posistion]
        if letter == guess:
            display_word[posistion] = letter

    if guess not in chosen_word:
        print(f"You guessed {guess} wrong. You lost a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print(f"the word I was looking for: {chosen_word}")
            print("You have lost the game")
    
    print(f"{' '.join(display_word)}")
    print("")
    print(stages[lives])

    if "_" not in display_word:
        end_of_game = True
        print("You have won the game!")
    