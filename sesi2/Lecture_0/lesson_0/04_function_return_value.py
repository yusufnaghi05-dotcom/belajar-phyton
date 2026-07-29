# Latihan: function dengan return value (pangkat)
def main():
    x = int(input("What is x? "))
    print("x squared is", square(x))

def square(n):
    return pow(n, 2)  # note: pow(n, 2) untuk kuadrat, bukan pow(n, 3)

main()