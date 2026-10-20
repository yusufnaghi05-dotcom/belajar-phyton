import sys

if len(sys.argv) != 2: 
    sys.exit("Too few command-line arguments")
if not sys.argv[1].endswith(".py"):
    sys.exit("Not a Python file")
if len (sys.argv) > 2:
    sys.exit("Too many command-line arguments")
    
try:
    with open(sys.argv[1]) as file:
        lines = file.readlines()
        count = 0
        for line in lines:
            if line.lstrip().startswith("#"):
                continue
            if line.strip():
                count += 1
        print(count)
except FileNotFoundError:
    sys.exit()