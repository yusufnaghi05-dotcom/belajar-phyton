def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    tanpa_dollar = d.replace("$", "")
    hasil = float(tanpa_dollar)
    return hasil
def percent_to_float(p):
    tanpa_percent = p.replace("%", "")
    angka = float(tanpa_percent)
    hasil= angka / 100
    return hasil

main()
