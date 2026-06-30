from modul import utils

FILE_PEMILIH = "data/pemilih.json"

def tambah_pemilih():
    print("\n=== REGISTRASI MANDIRI PEMILIH ===")
    
    daftar_pemilih = utils.load_data(FILE_PEMILIH)
    
    id_pemilih = input("Masukkan ID Pemilih baru (Wajib diawali 'PM', contoh: PM001): ").strip().upper()
    
    if not id_pemilih.startswith("PM") or not id_pemilih[2:].isdigit():
        print("GAGAL: Format ID salah! Wajib berawalan 'PM' dan diikuti angka. (Contoh: PM001)")
        return
        
    for pemilih in daftar_pemilih:
        if pemilih["id"] == id_pemilih:
            print("GAGAL: ID Pemilih sudah terdaftar di sistem!")
            return
    
    nama = input("Masukkan Nama Mahasiswa: ").strip()
    jurusan = input("Masukkan Jurusan/Prodi: ").strip()
    
    if not nama or not jurusan:
        print("GAGAL: Nama dan Jurusan tidak boleh kosong!")
        return 
    
    pemilih_baru = {
        "id": id_pemilih,
        "nama": nama,
        "jurusan": jurusan,
        "sudah_memilih": False
    }
    
    daftar_pemilih.append(pemilih_baru)
    utils.save_data(FILE_PEMILIH, daftar_pemilih)
    
    print(f"BERHASIL: Pemilih bernama '{nama}' sukses terdaftar dengan ID '{id_pemilih}'!")