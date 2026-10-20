import tabulate
import sys
import csv

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
if len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
if sys.argv[1].endswith(".txt"):
    sys.exit("Not a CSV file")
if not sys.argv[1].endswith(".csv"):
    sys.exit("Not a Python file")
data = []
try:
    with open(sys.argv[1]) as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append({"Regular Pizza": row["Regular Pizza"], "Small": row["Small"], "Large": row["Large"]})
except FileNotFoundError:
    sys.exit("File does not exist")
    
new_table = tabulate.tabulate(data)
print(new_table)
    
# import csv

# students = []

# with open("students.csv") as file:
#     reader = csv.DictReader(file)
#     for row in reader:
#         students.append({"name": row["name"], "home": row["home"]})

# for student in sorted(students, key=lambda student: student['name']):
#     print(f'{student["name"]} is in {student["home"]}')