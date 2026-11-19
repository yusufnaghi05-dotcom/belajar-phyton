from datetime import date
import inflect
p = inflect.engine()
def main():
    try:
        tanggal = input("Date of Birth: ")
        print(convert(tanggal))
    except ValueError:
        print("Invalid date")
def convert(x):
    tanggal_baru = date.fromisoformat(x)
    today = date.today()
    selisih = today - tanggal_baru
    jumlah_hari = selisih.days
    if jumlah_hari < 0: 
        raise ValueError
    menit = jumlah_hari * 24 * 60
    return f"{p.number_to_words(menit, andword="").capitalize()} minutes"

if __name__ == "__main__":
    main()