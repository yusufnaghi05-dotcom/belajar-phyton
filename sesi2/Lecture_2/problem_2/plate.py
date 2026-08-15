def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if len(s) < 2 or len(s) > 6:
        return False
    if not s[0:2].isalpha():
        return False

    sudah_ketemu_angka = False
    for x in s:
        if x.isalpha():
            if sudah_ketemu_angka == True:
                return False  
        if x.isdigit():
            if not sudah_ketemu_angka and x == "0":
                return False
            sudah_ketemu_angka = True 
        if not x.isalpha() and not x.isdigit():
            return False
    return True

main()