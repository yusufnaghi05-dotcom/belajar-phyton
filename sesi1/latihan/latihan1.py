def grade(nilai):
    if nilai >= 90 :
        print(f"nilai {nilai} mendapatkan grade A")
    elif nilai >= 80 and nilai <= 89:
        print(f"nilai {nilai} mendapatkan grade B")
    elif nilai >= 70 and nilai <= 79:
        print(f"nilai {nilai} mendapatkan grade C")
    elif nilai >= 60 and nilai <=69:
        print(f"nilai {nilai} mendapatkan grade D")
    else:
        print(f"nilai {nilai} mendapatkan grade E") 

nilai = int(input("masukkan nilai kamu : "))  
grade(nilai) 