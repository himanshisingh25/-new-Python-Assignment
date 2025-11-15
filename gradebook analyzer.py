# Name- Himanshi Singh
# Date : - 12/11/2025


import csv

print("Welcome to app !\n")

choice = input("choose Manual/csv Entry : ")
n= int(input("enter number of inputs : "))

marks = {}
grades = {}

if choice == "Manual":
    for i in range(n):
        n1 = input("name ? : ")
        n2 = int(input("marks ? : "))
        marks[n1] = n2
elif choice == "csv":
    with open('gradebook.csv', mode='a+') as file:
        csv_file = csv.writer(file)
        csv_file.writerow(['Name', 'Marks'])
        csv_file.writerow(['----', '-----'])
        for i in range(n):
            n1 = input("name ? : ")
            n2 = int(input("marks ? : "))
            marks[n1] = n2
            csv_file.writerow([n1, n2])

# Grades

for student, score in marks.items():
    if score >= 90:
        grades[student] = 'A'
    elif score >= 80:
        grades[student] = 'B'
    elif score >= 70:
        grades[student] = 'C'
    elif score >= 60:
        grades[student] = 'D'
    else:
        grades[student] = 'F'


def calculate_average(marks):
    total = sum(marks.values())
    count = len(marks)
    if count == 0:
        return 0 
    average = total / count
    return average

def calculate_median(marks):
    scores = list(marks.values())
    if not scores:
        return 0
    sorted_scores = sorted(scores)
    n = len(sorted_scores)
    mid = n // 2
    if n % 2 == 0:
        median = (sorted_scores[mid - 1] + sorted_scores[mid]) / 2
    else:
        median = sorted_scores[mid]
    return median

def find_max_score(marks_dict):
    return max(marks_dict.values())

def find_min_score(marks_dict):
    return min(marks_dict.values())

print(f"Average Score: {calculate_average(marks)}")
print(f"Median Score: {calculate_median(marks)}")
print(f"Maximum Score: {find_max_score(marks)}")
print(f"Minimum Score: {find_min_score(marks)}")
print(f"Grade Distribution: A: {sum(1 for g in grades.values() if g == 'A')}, B: {sum(1 for g in grades.values() if g == 'B')}, C: {sum(1 for g in grades.values() if g == 'C')}, D: {sum(1 for g in grades.values() if g == 'D')}, F: {sum(1 for g in grades.values() if g == 'F')} ")
print(f"passed : {sum(1 for g in grades.values() if g in ['A', 'B', 'C', 'D'])}, failed : {sum(1 for g in grades.values() if g == 'F')}")

while True:
    user_input = input("Do you want to continue and see the results table ? (yes/no) : ")
    if user_input.lower() == 'yes':
        print("\nResults Table:")
        print("{:<15} {:<10} {:<10}".format('Name', 'Marks', 'Grade'))
        print("-" * 35)
        for student in marks:
            print("{:<15} {:<10} {:<10}".format(student, marks[student], grades[student]))
        print()
    elif user_input.lower() == 'no':
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")