import random
num_grades = int(input("Enter the number of grades in the list: "))
grades = [random.randint(1, 100) for _ in range(num_grades)]
passing_grade = int(input("Enter the passing grade: "))
passGrades = [grade for grade in grades if grade >= passing_grade]
print(f"Original List: {grades}")
print(f"Updated List: {passGrades}")
