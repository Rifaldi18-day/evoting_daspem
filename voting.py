from modul import utils

FILE_PEMILIH = "data/pemilih.json"
FILE_CALON = "data/calon.json"

def lakukan_voting():
    print("\n=== PROSES VOTING (PENCOBLOSAN RAHASIA) ===")
    
    daftar_pemilih = utils.load_data(FILE_PEMILIH)
    daftar_calon = utils.load_data(FILE_CALON)
    
    if not daftar_calon:
        print("GAGAL: Surat suara kosong! Admin belum mendaftarkan calon ketua apa pun.")
        return

    id_pemilih = input("Masukkan ID Pemilih Anda: ").strip().upper()
    
    pemilih_ditemukan = None
    for p in daftar_pemilih:
        if p["id"] == id_pemilih:
            pemilih_ditemukan = p
            break
            
    if pemilih_ditemukan is None:
        print("GAGAL: ID Pemilih tidak terdaftar di sistem!")
        return
        
    if pemilih_ditemukan["sudah_memilih"] == True:
        print(f"GAGAL: Mahasiswa dengan ID {id_pemilih} SUDAH menggunakan hak suara!")
        print("Satu pemilih hanya diperbolehkan memilih satu kali.")
        return 
        
    print("\n--- SURAT SUARA: DAFTAR CALON KETUA ---")
    for c in daftar_calon:
        print(f"[{c['id']}] {c['nama']}")
        print(f"      Visi: {c['visi']}\n")
    print("---------------------------------------")
    
    id_calon = input("Masukkan ID Calon Ketua pilihan Anda: ").strip().upper()
    
    calon_ditemukan = None
    for c in daftar_calon:
        if c["id"] == id_calon:
            calon_ditemukan = c
            break
            
    if calon_ditemukan is None:
        print("GAGAL: ID Calon yang Anda masukkan tidak valid/tidak ada!")
        return 
        
    print(f"\nPilihan Anda: [{calon_ditemukan['id']}] - {calon_ditemukan['nama']}")
    konfirmasi = input("Apakah Anda yakin dengan pilihan ini? (Y/N): ").strip().upper()
    if konfirmasi != "Y":
        print("🔄 VOTING DIBATALKAN: Silakan ulangi proses jika ingin mengganti pilihan.")
        return

    pemilih_ditemukan["sudah_memilih"] = True
    
    calon_ditemukan["jumlah_suara"] += 1
    
    utils.save_data(FILE_PEMILIH, daftar_pemilih)
    utils.save_data(FILE_CALON, daftar_calon)
    
    print("\nSYSTEM NOTE: Log data pemilih dan database suara telah diperbarui secara terpisah.")
    print(f"BERHASIL: Hak suara '{pemilih_ditemukan['nama']}' sah terekam secara anonim. Terima kasih!")

def tampilkan_hasil():
    print("\n=== PEROLEHAN HASIL SUARA SEMENTARA ===")
    
    daftar_calon = utils.load_data(FILE_CALON)
    
    if not daftar_calon:
        print("Belum ada data calon ketua yang terdaftar.")
        return

    print("+" + "-"*12 + "+" + "-"*22 + "+" + "-"*16 + "+")
    print(f"| {'ID Calon':<10} | {'Nama Calon':<20} | {'Jumlah Suara':<12} |")
    print("+" + "-"*12 + "+" + "-"*22 + "+" + "-"*16 + "+")
    for c in daftar_calon:
        print(f"| {c['id']:<10} | {c['nama']:<20} | {c['jumlah_suara']:<12} |")
    print("+" + "-"*12 + "+" + "-"*22 + "+" + "-"*16 + "+")