import random

stages = [
    """
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
""",
    """
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
""",
    """
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
""",
    """
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
""",
    """
  +---+
  |   |
  O   |
      |
      |
      |
=========
""",
    """
  +---+
  |   |
      |
      |
      |
      |
=========
""",
]


end_of_game = False
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
lives = 6


print(f"the chosen word is: {chosen_word}")

display = []

word_lenght = len(chosen_word)
for _ in range(word_lenght):
    display += "_"

print(display)


while not end_of_game:
    guess = input("Guess a letter: ").lower()

    for posistion in range(word_lenght):
        letter = chosen_word[posistion]
        if letter == guess:
            display[posistion] = letter

    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You have lost the game")
            print(f"the word I was looking for: {chosen_word}")
    
    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You have won the game!")
    
    print(stages[lives])
