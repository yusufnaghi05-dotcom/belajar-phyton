import random

welcome_message = "WELCOME TO BITCOIN GAMES!"
cuypy_position = random.randint(1, 4)  
print("*****************************")
print(f"** {welcome_message} **")
print("*****************************")

nama_user = input("masukkan nama kamu: ")

bentuk_goa = "|_|"

goa_kosong = [bentuk_goa] * 4 #ini tetap harus kosong

goa = goa_kosong.copy()  #tempat baru cuypy 
 
goa[cuypy_position - 1] = "|0_0|" 


print(f'''
halo selamat datang {nama_user}!! Coba lihat perhatikan goa dibawah ini   
{" ".join(goa_kosong)}  
''')  

pilihan_user = int(input("Menurut kamu di goa nomor berapa CUYPY berada? [1 / 2 / 3 / 4]: ")) 

confirm_answer =input(f"apakah kamu yakin jawabannya adalah {pilihan_user}? [y/n]: ") 

if confirm_answer == "n":
    print("program dihentikan!") 
    exit() 
elif confirm_answer == "y": 
    if pilihan_user == cuypy_position:
        print(f"{" ".join(goa)} \n Selamat Kamu Menang!")
    else:
        print(f"{" ".join(goa)} \n Maaf kamu kalah!")    
else:
    print("Silahkan ulangi lagi programnya") 
    

