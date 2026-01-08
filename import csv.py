import csv

def sistem_penjualan_toko_mainan():
    print("====================================")
    print("🛒 Sistem Penjualan Toko Mainan 🤖")
    print("====================================")
    
    # List untuk menyimpan detail setiap item yang dibeli: [Nama Barang, Jumlah, Harga, Total Harga Item]
    transaksi = []
    subtotal = 0
    diskon = 0
    
    # --- 1. Looping Input Transaksi ---
    print("\n--- Input Transaksi Barang ---")
    while True:
        nama = input("Masukkan Nama Barang: ")
        
        # Validasi Input Jumlah
        while True:
            try:
                jumlah = int(input(f"Jumlah beli {nama}: "))
                if jumlah <= 0:
                    print("Jumlah harus lebih dari 0.")
                    continue
                break
            except ValueError:
                print("Input jumlah harus berupa angka.")

        # Validasi Input Harga
        while True:
            try:
                harga = int(input(f"Harga satuan {nama} (Rp): "))
                if harga < 0:
                    print("Harga tidak boleh negatif.")
                    continue
                break
            except ValueError:
                print("Input harga harus berupa angka.")
        
        # Hitung total harga per item
        total_harga_item = jumlah * harga
        
        # Tambahkan detail item ke list transaksi
        transaksi.append([nama, jumlah, harga, total_harga_item])
        
        # Tambahkan ke subtotal keseluruhan
        subtotal += total_harga_item
        
        # Tanyakan apakah ada barang lain
        jawab = input("Tambah barang lagi (Y/T)? ").upper()
        if jawab != 'Y':
            break

    # --- 2. Hitung Diskon dan Total Bayar ---
    
    # Logika diskon berdasarkan screenshot (sekitar baris 21-27)
    # Asumsi: Jika subtotal >= 50000, diskon 10%. Jika subtotal < 50000, diskon 5%.
    
    if subtotal >= 50000:
        diskon = 0.10  # 10%
    elif subtotal >= 10000:
        # Menambahkan kondisi ini karena diskon 5% mungkin hanya berlaku jika subtotal mencapai batas tertentu
        diskon = 0.05  # 5%
    else:
        diskon = 0.00 # Tidak ada diskon

    nilai_diskon = int(subtotal * diskon)
    total_bayar = subtotal - nilai_diskon
    
    # --- 3. Output Laporan di Console ---
    print("\n====================================")
    print("🧾 RINCIAN TRANSAKSI 🧾")
    print("====================================")
    
    # Header Tabel Transaksi
    print(f"{'Nama Barang':<20}{'Jumlah':>8}{'Harga':>10}{'Total':>12}")
    print("-" * 50)
    
    # Isi Tabel Transaksi
    for item in transaksi:
        nama_brg, jml, hrg, total = item
        print(f"{nama_brg:<20}{jml:>8}{hrg:>10,}{total:>12,}")

    print("-" * 50)
    print(f"{'SUBTOTAL':<40}{subtotal:>12,}")
    print(f"{'DISKON ({diskon*100:.0f}%)':<40}{nilai_diskon:>12,}")
    print("-" * 50)
    print(f"{'TOTAL BAYAR':<40}{total_bayar:>12,}")
    print("====================================")
    
    # --- 4. Simpan ke File CSV ---
    file_name = 'laporan_transaksi.csv'
    
    # Mode 'w' (write) akan membuat file baru atau menimpa yang sudah ada
    try:
        with open(file_name, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            
            # Tulis Header Transaksi
            writer.writerow(["Nama Barang", "Jumlah", "Harga", "Total"])
            
            # Tulis Data Transaksi (Looping item in transaksi)
            for item in transaksi:
                writer.writerow(item)
                
            # Tambahkan baris kosong untuk pemisah
            writer.writerow([]) 
            
            # Tulis Summary (Subtotal, Diskon, Total Bayar)
            writer.writerow(["SUBTOTAL", "", "", subtotal])
            writer.writerow([f"DISKON ({diskon*100:.0f}%)", "", "", nilai_diskon])
            writer.writerow(["TOTAL BAYAR", "", "", total_bayar])

        print(f"\n Data Transaksi berhasil disimpan ke {file_name}")

    except Exception as e:
        print(f"\n Terjadi error saat menyimpan file CSV: {e}")

# Panggil fungsi utama untuk menjalankan program
if __name__ == "__main__":
    sistem_penjualan_toko_mainan()