print("Hello to the BMI-Calculator!")
height = input("What is your height?\n")
weight = input("What is your weight?\n")

weight = int(weight)
height = float(height)

bmi = weight / height**2

bmi_as_int = int(bmi)

print(f"your BMI = {bmi_as_int}")