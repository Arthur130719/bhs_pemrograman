def tampilkan_menu_utama():
    print("Menu Utama:")
    print("1. Makanan")
    print("2. Minuman")
    print("3. Kembali")
    pilihan = input("Pilih menu: ")
    return pilihan

def tampilkan_menu_makanan():
    print("Menu Makanan:")
    print("1. Pecel Lele")
    print("2. Nasi Goreng")
    print("3. Kembali")
    pilihan = input("Pilih makanan: ")
    return pilihan

def tampilkan_menu_minuman():
    print("Menu Minuman:")
    print("1. Teh Manis")
    print("2. Air Mineral")
    print("3. Kembali")
    pilihan = input("Pilih minuman: ")
    return pilihan

def tampilkan_pilihan_pecel_lele():
    print("Pecel Lele:")
    print("1. Qty")
    print("2. Total")
    print("3. Kembali")
    pilihan = input("Pilih opsi: ")
    return pilihan

def tampilkan_pilihan_nasi_goreng():
    print("Nasi Goreng:")
    print("1. Qty")
    print("2. Total")
    print("3. Kembali")
    pilihan = input("Pilih opsi: ")
    return pilihan

def hitung_total_harga(qty, harga_per_unit):
    return qty * harga_per_unit

def main():
    while True:
        pilihan_utama = tampilkan_menu_utama()
        
        if pilihan_utama == "1":  # Makanan
            while True:
                pilihan_makanan = tampilkan_menu_makanan()
                
                if pilihan_makanan == "1":  # Pecel Lele
                    qty_pecel_lele = 0
                    harga_pecel_lele = 15000
                    
                    while True:
                        pilihan_pecel_lele = tampilkan_pilihan_pecel_lele()
                        
                        if pilihan_pecel_lele == "1":  # Qty
                            qty_pecel_lele = int(input("Masukkan jumlah Pecel Lele: "))
                            print(f"Jumlah Pecel Lele: {qty_pecel_lele}")
                        
                        elif pilihan_pecel_lele == "2":  # Total
                            total_harga = hitung_total_harga(qty_pecel_lele, harga_pecel_lele)
                            print(f"Total harga Pecel Lele: Rp{total_harga}")
                        
                        elif pilihan_pecel_lele == "3":  # Kembali
                            break
                
                elif pilihan_makanan == "2":  # Nasi Goreng
                    qty_nasi_goreng = 0
                    harga_nasi_goreng = 13000
                    
                    while True:
                        pilihan_nasi_goreng = tampilkan_pilihan_nasi_goreng()
                        
                        if pilihan_nasi_goreng == "1":  # Qty
                            qty_nasi_goreng = int(input("Masukkan jumlah Nasi Goreng: "))
                            print(f"Jumlah Nasi Goreng: {qty_nasi_goreng}")
                        
                        elif pilihan_nasi_goreng == "2":  # Total
                            total_harga = hitung_total_harga(qty_nasi_goreng, harga_nasi_goreng)
                            print(f"Total harga Nasi Goreng: Rp{total_harga}")
                        
                        elif pilihan_nasi_goreng == "3":  # Kembali
                            break
                
                elif pilihan_makanan == "3":  # Kembali
                    break
        
        elif pilihan_utama == "2":  # Minuman
            while True:
                pilihan_minuman = tampilkan_menu_minuman()
                
                if pilihan_minuman == "1":  # teh manis
                    qty_teh_manis = 0
                    harga_teh_manis = 3000
                    
                    while True:
                        pilihan_teh_manis = tampilkan_pilihan_teh_manis()
                        
                        if pilihan_teh_manis == "1":  # Qty
                            qty_teh_manis = int(input("Masukkan jumlah teh manis: "))
                            print(f"Jumlah teh manis: {qty_pecel_lele}")
                        
                        elif pilihan_teh_manis == "2":  # Total
                            total_harga = hitung_total_harga(qty_teh_manis, harga_teh_manis)
                            print(f"Total harga teh manis: Rp{total_harga}")
                        
                        elif pilihan_teh_manis == "3":  # Kembali
                            break
                
        elif pilihan_utama == "3":  # Kembali
            print("Terima kasih telah menggunakan program ini.")
            break

if __name__ == "__main__":
    main()
