import csv

def main():
    fruit = input("Item: ").lower()
    if calories(fruit):
        print(f"Calories: {calories(fruit)}")
    else:
        pass
        
def calories(x):
    with open("nutrition.csv") as file:
        reader = csv.reader(file) 
        for row in reader:
            if row[0] == x:
                return int(row[1])

main()