import math

print("How big is your wall?\n")

height = float((input("What is the height?\n")))
width = float((input("What is the height?\n")))

outcome = height and width

def cover(outcome):
    can_covers = 5

    coverage = height * width / can_covers
    rounded_coverage = math.ceil(coverage)
    print(f"You'll need '{rounded_coverage}', of cans to paint the wall")

cover(outcome)