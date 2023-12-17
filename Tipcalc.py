print("Welcome to the tip calculator!")
bill = float(input("What is the total amound to pay?\n"))
tip = int(input("What will the tip be?\n"))
people = int(input("How many people are in the group? \n"))

tip_precent = tip / 100
total_tip = bill * tip_precent
total_bill = bill + total_tip
bill_person = total_bill / people
final_amount = round(bill_person, 2)

print(f"Each motherfocker will be paying: ${final_amount}")
