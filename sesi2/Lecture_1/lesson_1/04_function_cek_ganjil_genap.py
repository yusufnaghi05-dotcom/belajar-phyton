# Latihan: cek ganjil/genap
# Evolusi belajar (dari versi paling sederhana ke versi pakai function):
#   v1: langsung if/else tanpa function
#   v2: pakai function is_even() dengan if/else di dalamnya
#   v3: pakai function is_even() diringkas jadi 1 baris return kondisi

def main():
    x = int(input("What is x? "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")


def is_even(n):
    return n % 2 == 0


main()