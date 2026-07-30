
def main():
    waktu = input("What time is it? ")
    waktu_akhir = convert(waktu)
    if waktu_akhir >= 7.0 and waktu_akhir <= 8.0:
        print("breakfast time")
    elif waktu_akhir >= 12.0 and waktu_akhir <= 13.0:
        print("lunch time")
    elif waktu_akhir >= 18.0 and waktu_akhir <= 19.0:
        print("dinner time")
    else:
        pass
def convert(time): 
    bagian = time.split(":")
    jam = float(bagian [1-1])
    menit = float(bagian [2-1])
    hasil = jam + (menit / 60)
    return hasil
if __name__ == "__main__":
    main()