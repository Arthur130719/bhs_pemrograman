angka_1 = float(input("Masukkan angka pertama: "))
angka_2 = float(input("Masukkan angka kedua: "))

penjumlahan = angka_1 + angka_2
pengurangan = angka_1 - angka_2
perkalian = angka_2 * angka_2

if angka_kedua != 0:
    pembagian = angka_1 / angka_2
else:
    pembagian = "Tidak bisa dibagi nol"

print("Hasil Penjumlahan:", penjumlahan)
print("Hasil Pengurangan:", pengurangan)
print("Hasil Perkalian:", perkalian)
print("Hasil Pembagian:", pembagian)
