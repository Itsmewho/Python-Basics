student_heights = []
choise = True

student_heights.append(input("What is the student height in cm?\n"))

choise = input("Do you want to add more students? (y or n)\n")
if choise == "y":
    while choise == "y":
        student_heights.append(input("What is the student height in cm?\n"))
        choise = input("Do you want to add more students? (y or n)\n")

print(student_heights)
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

total_height = 0
for height in student_heights:
    total_height += height
print(f"total height = {total_height}")

number_of_students = 0
for student in student_heights:
    number_of_students += 1
print(f"number of students = {number_of_students}")

average_height = round(total_height / number_of_students)
print(f"average height = {average_height}")
