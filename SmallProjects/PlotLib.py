import os

clear = lambda: os.system("cls")

game = False
pronoun = ""

print("Hello welcome to some sort of plotlib.")


while game !=True:
    while True:
        story = input(f"Would you like a story?\nType in yes or no: ")
        if story.startswith("y"):
            clear()
            pronoun = input("What is your name? \n")
            clear()
            noun = input("What type of thing are you? \n")
            clear()
            adjective = input("What is an adjective that you have? \n")
            clear()
            verb = input("give me a verb!? \n ")
            clear()
            
            print(f"Hello {pronoun}!\n")
            print(f"I hear you are some kind of super {noun}\n")
            print(f"A {adjective}-{noun}\n")
            print(f"That likes to {verb}")
            break
        if story.startswith("n"):
            game = True
            print("Till next time!")
            break

