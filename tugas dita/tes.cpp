#include <iostream>

using namespace std;

int main() {
    int n;
    cout << "Masukkan jumlah baris: ";
    cin >> n;

    for (int i = 1; i <= n; i++) {
        // Menampilkan spasi
        for (int j = n; j > i; j--) {
            cout << " ";
        }
        // Menampilkan bintang
        for (int k = 1; k <= i; k++) {
            cout << "*";
        }
        cout << "\n";
    }
    return 0;
}