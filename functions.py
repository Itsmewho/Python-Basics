import math

print("How big is your wall?\n")

height = float((input("What is the height?\n")))
width = float((input("What is the height?\n")))

def cover():
    can_covers = 5

    coverage = height * width / can_covers
    rounded_coverage = math.ceil(coverage)
    print(f"You'll need '{rounded_coverage}', of cans to paint the wall")

cover()