import sys
def main():
    item = get_price()
    item1 = (f"{item:.2f}")
    print(f"${item1}")
def get_price():
    while True:
        try:
            a = (input("Item: ")).title()
            food = {
                "Baja Taco": 4.25,
                "Burrito": 7.50,
                "Bowl": 8.50,
                "Nachos": 11.00,
                "Quesadilla": 8.50,
                "Super Burrito": 8.50,
                "Super Quesadilla": 9.50,
                "Taco": 3.00,
                "Tortilla Salad": 8.00
            }
            if a in food:
                ab = float((f"{food[a]}"))
                return ab
        except ValueError:
            continue
        except EOFError:
            sys.exit()

main()