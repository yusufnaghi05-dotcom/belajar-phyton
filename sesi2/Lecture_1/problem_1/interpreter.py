question = input("Expressions: ")

parts = question.split()
x = int(parts[1-1])
y = (parts[2-1])
z = int(parts[3-1])


if y == "+":
    hasil = x + z
elif y == "-":
    hasil = x - z
elif y == "/":
    hasil = x / z
elif y == "*":
    hasil = x * z
hasil_akhir = float(hasil)
print(f"{hasil_akhir:.1f}")