// NAMA = Dita Yolanda
// NIM = 231011750008
// KODE KELAS = 01sifp001

#include <iostream>
using namespace std;

void tampilkanMenu() {
    cout << "\n======== MENU ========\n";
    cout << "1. Cek Kategori Usia\n";
    cout << "2. Keluar Program\n";
    cout << "Pilih Menu: ";
}

void cekUsia(int usia) {
    if (usia <= 0) {
        cout << "Usia Tidak Valid. Silakan Coba Lagi.\n";
    } 
    else if (usia <= 5) {
        cout << "Usia Tersebut Termasuk Kategori Balita\n";
    } 
    else if (usia <= 11) {
        cout << "Usia Tersebut Termasuk Kategori Kanak Kanak\n";
    }
    else if (usia <= 20) {
        cout << "Usia Tersebut Termasuk Kategori Remaja\n";
    }
    else if (usia <= 25) {
        cout << "Usia Tersebut Termasuk Kategori Pra Dewasa\n";
    }
    else if (usia <= 45) {
        cout << "Usia Tersebut Termasuk Kategori Dewasa\n";
    }
    else if (usia <= 65) {
        cout << "Usia Tersebut Termasuk Kategori Lansia\n";
    }
    else {
        cout << "Usia Tersebut Termasuk Kategori Manula\n";
    }
}

int main() {
    int pilihan;
    int usia;

    do {
        tampilkanMenu();
        cin >> pilihan;

        switch(pilihan) {
            case 1:
                cout << "Masukkan Usia: ";
                cin >> usia;
                cekUsia(usia);
                break;
            case 2:
                cout << "Keluar Dari Program, Terima Kasih\n";
                break;
            default:
                cout << "Pilihan Menu Tidak Valid. Silakan Coba Lagi.\n";
        }
    } while (pilihan != 2);

    return 0;
}
