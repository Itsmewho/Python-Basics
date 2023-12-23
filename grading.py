import os

clear = lambda: os.system("cls")


student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}

adding_students = False


def cat_students(grading):
    highest_student = 0
    name = ""

    # check higest for best student
    for student_name in grading:
        grade_student = grading[student_name]
        if grade_student > highest_student:
            highest_student = grade_student
            name = student_name
    print(f"\nThe best student is {name}, with a score of: {grade}\n")

    # check lowest for last
    lowest = min(student_scores, key=student_scores.get)

    print(f"\nThe lowest score: {lowest}\n")

    for student_name in grading:
        student_grade = grading[student_name]
        if student_grade > 91:
            grading[student_name] = "Oustanding"
        if student_grade <= 90:
            grading[student_name] = "Exeeds Expectations"
        if student_grade <= 80:
            grading[student_name] = "Acceptable"
        if student_grade <= 70:
            grading[student_name] = "You suck"
    print(f"\nAll students scores: {student_scores}\n")


while adding_students != True:
    name = input("What is the name is the student?\n")
    grade = int(input("What is the grade?\n"))
    student_scores[name] = grade
    while True:
        response = input("Do you have more? (y or n)")
        if response.startswith("y"):
            clear()
            break
        if response.startswith("n"):
            cat_students(student_scores)
            adding_students = True
            break
