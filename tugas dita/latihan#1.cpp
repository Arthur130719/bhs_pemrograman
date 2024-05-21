// NAMA = Dita Yolanda
// NIM = 231011750008
// KODE KELAS = 01sifp001

#include <iostream>
using namespace std;

int main() {
    int usia;
    cout << "Masukan Usia : ";
    cin >> usia;

    if (usia == 0) {
    	cout << "Usia Tidak Valid Silakan Masukan Lagi";
	}
    else if (usia <= 5) {
        cout << "Balita";
    } 
    else if (usia <= 11) {
        cout << "Kanak Kanak";
    }
    else if (usia <= 20) {
        cout << "Remaja";
    }
    else if (usia <= 25) {
        cout << "Pra Dewasa";
    }
    else if (usia <= 45) {
        cout << "Dewasa";
    }
    else if (usia <= 65) {
        cout << "Lansia";
    }
    else {
        cout << "Manula";
    } 
}