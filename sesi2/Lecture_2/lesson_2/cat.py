# x = 3
# while x != 0:
#     print("meow")
#     x = x - 1

# x = 0
# while x < 3:
#     print("meow")
#     x += 

# for i in range(3):
#     print("meow")

# print("meow\n" *3, end="")

# while True:
#     n = int(input("What is n? "))
#     if n > 0 :
#         break

# for _ in range (n):
#     print("meow")
def main():
    number = get_number()
    meow(number)
    
def get_number():
    while True:
        n = int(input("What is n? "))
        if n > 0:
            break
    return n 
    
def meow(n):
    for x in range(n):
        print("meow")
    
main()