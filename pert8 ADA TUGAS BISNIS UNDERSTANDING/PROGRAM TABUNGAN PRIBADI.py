import sqlite3
from datetime import datetime

conn = sqlite3.connect('savings_app.db')
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS savings
             (id INTEGER PRIMARY KEY, date TEXT, amount REAL)''')

def add_savings(date, amount):
    c.execute("INSERT INTO savings (date, amount) VALUES (?, ?)", (date, amount))
    conn.commit()

def delete_savings(entry_id):
    c.execute("DELETE FROM savings WHERE id = ?", (entry_id,))
    conn.commit()

def reset_savings():
    c.execute("DELETE FROM savings")
    conn.commit()

def get_total_savings():
    c.execute("SELECT id, date, amount FROM savings")
    savings = c.fetchall()
    return savings

def main():
    while True:
        print("PROGRAM CATATAN TABUNGAN PRIBADI\n")
        print("1. Tambah Catatan Tabungan")
        print("2. Lihat Catatan Saldo Tabungan")
        print("3. Hapus data Cacatan Tabungan")
        print("4. Reset Semua Data Cacatan Tabungan")
        print("5. Keluar")
        
        choice = input("Pilih opsi: ")
        
        if choice == '1':
            date = input("Masukkan tanggal (TAHUN-BULAN-TANGGAL): ")
            amount = float(input("Masukkan jumlah nominal yang ingin di tabungkan: "))
            add_savings(date, amount)
            print("Tabungan berhasil ditambahkan!")
        
        elif choice == '2':
            savings = get_total_savings()
            print("\nSaldo Tabungan Anda:")
            total = 0
            for entry_id, date, amount in savings:
                total += amount
                print(f"ID: {entry_id}, Tanggal: {date}, Jumlah: {amount}")
            print(f"Total Saldo: {total}")
        
        elif choice == '3':
            savings = get_total_savings()
            print("\nSaldo Tabungan Anda:")
            for entry_id, date, amount in savings:
                print(f"ID: {entry_id}, Tanggal: {date}, Jumlah: {amount}")
            entry_id = int(input("Masukkan ID tabungan yang ingin dihapus: "))
            delete_savings(entry_id)
            print("Tabungan berhasil dihapus!")
        
        elif choice == '4':
            confirmation = input("Apakah Anda yakin ingin mereset semua tabungan? (y/n): ")
            if confirmation.lower() == 'y':
                reset_savings()
                print("Semua tabungan berhasil direset!")
        
        elif choice == '5':
            print("PROGRAM DIHENTIKAN CATATAN SALDO AKAN TERSIMPAN OTOMATIS PADA PROGRAM INI, TERIMAKASIH..")
            break
        
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()
