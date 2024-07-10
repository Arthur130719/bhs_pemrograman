#include <iostream>

using namespace std;

void menu();
void tambah();
void kurang();
void kali();
void bagi();

int main() {
    menu();
    return 0;
}

void menu() {
    cout << "MENU:" << endl;
    cout << "1. Tambah" << endl;
    cout << "2. Kurang" << endl;
    cout << "3. Kali" << endl;
    cout << "4. Bagi" << endl;
}

void tambah() {
    cout << "Tambah" << endl;
}

void kurang() {
    cout << "Kurang" << endl;
}

void kali() {
    cout << "Kali" << endl;
}

void bagi() {
    cout << "Bagi" << endl;
}
