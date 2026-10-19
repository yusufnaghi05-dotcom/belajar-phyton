# with open('students.csv') as file:
#     for line in file:
#         name, house = line.rstrip().split(',')
#         print(f'{name} is in {house}')

# students = []

# with open('students.csv') as file:
#     for line in file:
#         name, house = line.rstrip().split(',')
#         students.append(f'{name} is in {house}')
        
# for student in sorted(students):
#     print(student)


# students = []

# with open('students.csv') as file:
#     for line in file:
#         name, house = line.rstrip().split(',')
#         student = {}
#         student['name'] = name
#         student['house'] = house
#         students.append(student)

# for student in sorted(students, key=lambda student: student['name']):
#     print(f'{student['name']} is in {student['house']}')

# students = []

# with open('students.csv') as file:
#     for line in file:
#         name, house = line.rstrip().split(',')
#         student = {'name': name, 'house': house}
#         students.append(student)

# def get_name(x):
#     return student['name']

# for student in sorted(students, key=get_name, reverse=False):
#     print(f'{student['name']} is in {student['house']}')

# import csv

# students = []

# with open("students.csv") as file:
#     reader = csv.DictReader(file)
#     for row in reader:
#         students.append({"name": row["name"], "home": row["home"]})

# for student in sorted(students, key=lambda student: student['name']):
#     print(f'{student["name"]} is in {student["home"]}')

# import csv

# name = input("What is your name? ")
# home = input("Where is your home? ")

# with open("students.csv", "a", newline="") as file:
#     writer = csv.writer(file)
#     writer.writerow([name, home])

import csv

name = input("What is your name? ")
home = input("Where is your home? ")

with open("students.csv", "a", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "home"])
    writer.writerow({"home": home, "name": name})
    