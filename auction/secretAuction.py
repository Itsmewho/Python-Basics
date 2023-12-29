import sys

sys.path.append("Auction")

import os

clear = lambda: os.system("cls")

from art import logo

print(logo)
print("\n Wolcome to the auction \n")


bids = {}
end_auction = False


def find_highest(record):
    highst_amount = 0
    name = ""
    for bidder in record:
        bid_amount = record[bidder]
        if bid_amount > highst_amount:
            highst_amount = bid_amount
            name = bidder
    print(f"The highest bidder is: {name}, with a bid of: {amount} ")

# make a while loop for the auction

while end_auction != True:
    name = input("What is your name?")
    amount = int(input("What is the amount you want to bid?"))
    bids[name] = amount
    while True:
        response = input("Any more bidders? Type in (y or n)").lower()
        if response.startswith("y"):
            clear()
            break #Don't forget this one :P
        if response.startswith("n"):
            find_highest(bids)
            end_auction = True
            break