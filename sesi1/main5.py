from libs import welcome_message, exit_program
from games import cuypy 
from tools import warung
import sys 

def menu():
    user_option = int(input(f"menu program:\n1. Games CUYPY\n2. Warung Mini\n3. Keluar Program\n\nsilahkan pilih: "))
    
    if user_option == 1: 
        cuypy.start()
    elif user_option == 2:
        warung.start()
    elif user_option == 3:
        exit_program()
        sys.exit()
        
    else:
        print("Hanya Boleh Memilih Yang Tersedia Di Menuuu!")

def main():
    welcome_message() 
    menu()
    
if __name__ == "__main__":
    main() 