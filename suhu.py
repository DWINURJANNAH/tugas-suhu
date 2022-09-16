print("\nKONVERTER SATUAN SUHU\n")

print("=====Konversi Celcius=====")

celcius = float(input("Masukkan nilai Celcius : "))
fahrenheit = (9 / 5) * celcius + 32
reamur = (4 / 5) * celcius
kelvin = celcius + 273

# KONVERSI CELCIUS
print("Nilai Celcius : ", celcius, "C")
print("Nilai dalam fahrenheit :", fahrenheit, "F")
print("Nilai dalam reamur :", reamur, "R")
print("Nilai dalam Kelvin :", kelvin, "K")
