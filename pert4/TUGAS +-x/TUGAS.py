def tambah(angka1, angka2):
    return angka1 + angka2

def kurang(angka1, angka2):
    return angka1 - angka2

def kali(angka1, angka2):
    return angka1 * angka2

def bagi(angka1, angka2):
    if angka2 == 0:
        return "Error: Pembagian dengan nol tidak dapat dilakukan"
    else:
        return angka1 / angka2

def main():
    print("Pilih operasi:")
    print("1. Tambah")
    print("2. Kurang")
    print("3. Kali")
    print("4. Bagi")
    pilihan = input("Masukkan pilihan : ")

    if pilihan not in ['1', '2', '3', '4']:
        print("Pilihan tidak valid")
        return

    angka1 = float(input("Masukkan angka 1: "))
    angka2 = float(input("Masukkan angka 2: "))

    if pilihan == '1':
        print("Hasil penjumlahan:", tambah(angka1, angka2))
    elif pilihan == '2':
        print("Hasil pengurangan:", kurang(angka1, angka2))
    elif pilihan == '3':
        print("Hasil perkalian:", kali(angka1, angka2))
    elif pilihan == '4':
        print("Hasil pembagian:", bagi(angka1, angka2))

if __name__ == "__main__":
    main()
