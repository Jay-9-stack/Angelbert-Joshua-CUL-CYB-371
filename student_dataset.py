
import csv

# Fictional student dataset
students = [
    ["STU001", "Computer Science", 300, 85, 78],
    ["STU002", "Mass Communication", 200, 90, 82],
    ["STU003", "Accounting", 100, 75, 68],
    ["STU004", "Computer Science", 400, 95, 88],
    ["STU005", "Business Administration", 300, 80, 74],
    ["STU006", "Economics", 200, 70, 65],
    ["STU007", "Computer Science", 200, 88, 91],
    ["STU008", "Political Science", 100, 92, 85],
    ["STU009", "Accounting", 400, 78, 72],
    ["STU010", "Mass Communication", 300, 84, 80]
]

# Dataset headings
headers = [
    "Student ID",
    "Department",
    "Level",
    "Attendance Percentage",
    "Average Examination Score"
]

# Create CSV file
with open("student_dataset.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(headers)
    writer.writerows(students)

print("Student dataset created successfully!")
