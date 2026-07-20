import sys
import os
sys.path.append(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
)
import main5
from libs import exit_program
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
        kembali_menu = input("Kembali ke menu? [y/n]: ")
        if kembali_menu == "y":
            main5.menu()
        else: 
            exit_program()
            sys.exit()
        # if play_again == "y":
        #     main5.menu()
          
        #   else:
        #     exit_program()
        #     sys.exit()

if __name__ =="__main__":
    start()
