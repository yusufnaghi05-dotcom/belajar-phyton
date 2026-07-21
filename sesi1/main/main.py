import random

welcome_message = "WELCOME TO BITCOIN GAMES!"
bitcoin_position = random.randint(1, 4)  
print("*****************************")
print(f"** {welcome_message} **")
print("*****************************")

nama_user = input("masukkan nama kamu: ")

print(f'''
halo selamat datang {nama_user}!! Coba lihat 4 kolom ini, salah satu kolomnya 
terdapat bitcoin  
|_| |_| |_| |_| 
''')  
tebak = False
percobaan = 0 
while not tebak: 
    pilihan_user = int(input ("Menurut kamu di kolom nomor berapa bitcoin berada? [1 / 2 / 3 / 4]: "))  
    print( ) 
    if pilihan_user == 1:
        print("Kamu telah memilih kolom 1")
    elif pilihan_user == 2:
        print("Kamu telah memilih kolom 2")
    elif pilihan_user == 3:
        print("Kamu telah memilih kolom 3")
    else:
        print("Kamu telah memilih kolom 4") 
    print( )
    konfirmasi = input("Apakah kamu yakin? [ ya / tidak]").lower() 
    print( ) 
    if konfirmasi == "tidak":
        print("Oke, silahkan pilih lagi.\n")   
        continue  
    
    percobaan += 1  
    if pilihan_user == bitcoin_position:
        print(f"SELAMAT KAMU MENANG {nama_user} kamu menang! posisi bitcoin ada di kolom nomor {bitcoin_position} dan pilihanmu adalah kolom nomor {pilihan_user}")
        print( )  
        print(f"Kamu berhasil dalam percobaan {percobaan} percobaan")  
        tebak = True 
    else:
        print(f"KAMU SALAH! bitcoin ngga ada di situ, coba lagi!")  
        print( ) 

