from modul import utils

FILE_CALON = "data/calon.json"

def tambah_calon():
    print("\n=== PANEL ADMIN: TAMBAH DATA CALON KETUA ===")
    
    daftar_calon = utils.load_data(FILE_CALON)
    
    id_calon = input("Masukkan ID Calon baru (Wajib diawali 'CL', contoh: CL001): ").strip().upper()
    
    if not id_calon.startswith("CL") or not id_calon[2:].isdigit():
        print("GAGAL: Format ID salah! Wajib berawalan 'CL' dan diikuti angka. (Contoh: CL001)")
        return
        
    for calon in daftar_calon:
        if calon["id"] == id_calon:
            print("GAGAL: ID Calon sudah terdaftar di sistem!")
            return
            
    nama = input("Masukkan Nama Calon Ketua: ").strip()
    visi = input("Masukkan Visi & Misi Calon: ").strip()
    
    if not nama or not visi:
        print("GAGAL: Nama dan Visi Misi Calon tidak boleh kosong!")
        return
    
    calon_baru = {
        "id": id_calon,
        "nama": nama,
        "visi": visi,
        "jumlah_suara": 0 
    }
    

    daftar_calon.append(calon_baru)
    utils.save_data(FILE_CALON, daftar_calon)
    
    print(f"BERHASIL: Calon ketua bernama '{nama}' sukses ditambahkan dengan ID '{id_calon}'!")