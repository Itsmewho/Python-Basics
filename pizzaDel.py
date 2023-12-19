print("Thank you for choosing Python pizza Deliveries!")
size = input("What size pizza do you want? s,m or l ?\n")

bill = 0

if size == "s":
    bill += 15
if size == "m":
    bill += 20
if size == "l":
    bill += 25
elif size == "":
    print("No choice is made")
print(f"Your bill is ${bill}")

add_pepperoni = input("Do you want pepperoni?   y or n ?\n")
if size == "s" and add_pepperoni == "y":
    bill += 2
if size == "m" or size == "l" and add_pepperoni == "y":
    bill += 3
if add_pepperoni == "" or add_pepperoni == "n":
    print("No pepperoni will be added.")
print(f"your bill is ${bill}")

extra_cheese = input("Do you want extra cheese? y or n ?\n")
if extra_cheese == "y":
    bill += 1
if extra_cheese == "" or extra_cheese == "n":
    print("No cheese will be added.")
print(f"your final bill is ${bill}")
