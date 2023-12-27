# my own blackjack version:
import sys

sys.path.append("cards")

import os

clear = lambda: os.system("cls")

import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
game_over = True
