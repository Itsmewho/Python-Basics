print("Hello to the BMI-Calculator!")
height = float(input("What is your height?\n"))
weight = int(input("What is your weight?\n"))

bmi = weight / (height * height)

bmi = round(bmi, 2)

if bmi < 18.5:
    print("Your BMI is lower then 18.5 you are underweight")
elif bmi < 25:
    print("Your BMI is between 18.5 and 25. You have an normal weight!")
elif bmi < 30:
    print("Your BMI is between the range of 25 and 30 you have a little overweight")
elif bmi < 35:
    print("Your BMI is between 30 and 35, you have some weight on you!")
else:
    print("You are fat as fuck!")


print(f"your BMI = {bmi}")
