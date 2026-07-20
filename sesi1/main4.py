import random
from libs import welcome_message  

welcome_message("SELAMAT DATANG DI CUYPY")  

nama_user = input("masukkan nama kamu: ")

while nama_user == "":
    nama_user = input("isi dulu nama anda: ")


while True:
    cuypy_position = random.randint(1, 4)    
    bentuk_goa = "|_|"

    goa_kosong = [bentuk_goa] * 4 #ini tetap harus kosong

    goa = goa_kosong.copy()  #tempat baru cuypy  
    
    goa[cuypy_position - 1] = "|0_0|"   

    goa_kosong = " ".join(goa_kosong)

    goa = " ".join(goa) 
    print(f'''
    halo selamat datang {nama_user}!! Coba lihat perhatikan goa dibawah ini   
    {goa_kosong}   
    ''')  
    while True: 
        try:
            pilihan_user = int(input("Menurut kamu di goa nomor berapa CUYPY berada? [1 / 2 / 3 / 4]: ")) 
            if pilihan_user in range(1, 5):
                break
            else:
                print("Masukkan angka (1-4)")
        except ValueError:
            print("Masukkan angka(1-4)") 
    confirm_answer =input(f"apakah kamu yakin jawabannya adalah {pilihan_user}? [y/n]: ") 

    if confirm_answer == "n":
        print("program dihentikan!") 
        exit() 
    elif confirm_answer == "y": 
        if pilihan_user == cuypy_position:
            print(f"{goa} \n Selamat Kamu Menang!")
        else:
            print(f"{goa} \n Maaf kamu kalah!")    
    else:
        print("Silahkan ulangi lagi programnya") 
    
    play_again = input("\napakah ingin melanjutkan gamenya lagi? [y/n]")
    if play_again == "n":
        break
    
print("Program selesai")


