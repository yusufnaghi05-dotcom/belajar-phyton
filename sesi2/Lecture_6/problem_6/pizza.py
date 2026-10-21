import tabulate
import sys
import csv

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
if len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
if not sys.argv[1].endswith(".csv"):
    sys.exit("Not a CSV file")
data = []

try:
    with open(sys.argv[1]) as file:
        reader = csv.DictReader(file)
        header = reader.fieldnames
        for row in reader:
            data.append(row)
except FileNotFoundError:
    sys.exit("File does not exist")
    
new_table = tabulate.tabulate(data, headers="keys", tablefmt="grid")
print(new_table)