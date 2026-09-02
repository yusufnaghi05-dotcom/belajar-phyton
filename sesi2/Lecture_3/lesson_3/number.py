# def main():
#     x = get_int("What is x? ")
#     print(f"x is {x}")

# def get_int(prompt):
#     while True:
#         try:
#             return int(input(prompt))
#         except ValueError:
#             pass
    
# main()
def main():
    x = get_int()
    print(f"x is {x}")

def get_int():
    while True:
        try:
            x = int(input("What is x?"))
        except ValueError:
            pass
        else:
            return x

main()
    
