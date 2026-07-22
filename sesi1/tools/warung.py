import sys 
import os



def start():
    while True:
        print("Naghi mempunyai uang 10000, lalu ia membeli pulpen seharga 8000")
        kembalian = int(input(f"Berapa kembaliannya yang diterima Naghi?: "))
        if kembalian == 2000:
            print("\nKamu benar")
            break
        else:
            print("Jawaban salah, coba ulangi lagi\n")
    while True:
        kembali_menu = input("Kembali ke menu? [y/n]: ").lower()
        if kembali_menu in ["y", "yes", "ya", "iya"]:
            import sesi1.main.main5
            sesi1.main.main5.menu()
            break
        elif kembali_menu in ["n", "no", "tidak", "ga", "gak"]:
            from sesi1.tools.libs import exit_program
            exit_program()
            sys.exit()
        else: 
            print("Masukkan y atau n saja")
 
if __name__ =="__main__":
    start()
