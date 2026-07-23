import random
def start():
    while True:
        cuypy_position = random.randint(1, 4)    
        bentuk_goa = "|_|"

        goa_kosong = [bentuk_goa] * 4 #ini tetap harus kosong

        goa = goa_kosong.copy()  #tempat baru cuypy  
        
        goa[cuypy_position - 1] = "|0_0|"   

        goa_kosong = " ".join(goa_kosong)

        goa = " ".join(goa) 
        print(f"Coba lihat perhatikan goa dibawah ini \n \n {goa_kosong} \n")  
        while True: 
            try:
                pilihan_user = int(input("Menurut kamu di goa nomor berapa CUYPY berada? [1 / 2 / 3 / 4]: ")) 
                if pilihan_user in range(1, 5):
                    break
                else:
                    print("Masukkan angka (1-4)")
            except ValueError:
                print("Masukkan angka(1-4)")  
        
        if pilihan_user == cuypy_position:
            print(f"{goa} \n Selamat Kamu Menang!")
        else:
            print(f"{goa} \n Maaf kamu kalah!")    
    
        
        play_again = input("\napakah ingin melanjutkan gamenya lagi? [y/n]")
        if play_again == "n":
            import sesi1.main.main5
            sesi1.main.main5.menu()

if __name__ == "__main__":
    start()