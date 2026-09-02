def main():
    a = get_b()
    if a <= 1:
        print("E")
    elif a >= 99:
        print("F")
    else:
        print(f"{a}%")
def get_b():
    while True:
        try:
            a = input("Fraction: ").split("/")
            a1 = int(a[0])
            a2 = int(a[1])
            if a1 < 0 or a2 <= 0 or a1 > a2:
               continue
           
            ax = a1 / a2 * 100
            axy = round(ax)
            return axy
        except ValueError:
            continue

main()