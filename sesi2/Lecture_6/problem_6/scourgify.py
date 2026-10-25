import sys
import csv

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
if len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
if not sys.argv[1].endswith(".csv"):
    sys.exit("Not a CSV file")
if not sys.argv[2].endswith(".csv"):
    sys.exit("Not a CSV file")
    
data = []

try:
    with open(sys.argv[1]) as file:
        reader = csv.DictReader(file)
        header = reader.fieldnames
        for row in reader:
            data.append(row)
except FileNotFoundError:
    sys.exit("Could not read input")

new_data = []
for row in data:
    name = row["name"]
    house = row["house"]
    parts = name.split(", ")
    first_part = parts[0]
    second_part = parts[1]
    new_data.append({"first": second_part, "last": first_part, "house": house})

try:
    with open(sys.argv[2], "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["first" , "last", "house"])
        writer.writeheader()
        writer.writerows(new_data)
                 
except FileNotFoundError:
    sys.exit("Could not read input")

    