# Latihan: function dengan if/elif/else dan return string
def main():
    harga_jual = int(input("Harga jual: "))
    harga_modal = int(input("Harga modal: "))
    print(cek_untung_rugi(harga_jual, harga_modal))

def cek_untung_rugi(jual, modal):
    if jual > modal:
        return "Untung"
    elif jual == modal:
        return "Balik modal tanpa keuntungan"
    else:
        return "Rugi"

main()