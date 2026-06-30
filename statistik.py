from modul import utils

FILE_PEMILIH = "data/pemilih.json"
FILE_CALON = "data/calon.json"

def tampilkan_statistik():
    print("\n=== PANEL ADMIN: ANALISIS STATISTIK PEMILU ===")
    
    daftar_pemilih = utils.load_data(FILE_PEMILIH)
    daftar_calon = utils.load_data(FILE_CALON)
    
    total_pemilih = len(daftar_pemilih)
    
    sudah_memilih = 0
    for p in daftar_pemilih:
        if p["sudah_memilih"] == True:
            sudah_memilih += 1
            
    golput = total_pemilih - sudah_memilih
            
    if total_pemilih > 0:
        persentase_hadir = (sudah_memilih / total_pemilih) * 100
        persentase_golput = (golput / total_pemilih) * 100
    else:
        persentase_hadir = 0.0
        persentase_golput = 0.0
        
    skala_bar = int(persentase_hadir // 10)
    bar_visual = "█" * skala_bar + "░" * (10 - skala_bar)
        
    print(f"Total Pemilih Terdaftar : {total_pemilih} mahasiswa")
    print(f"Jumlah yang Sudah Hadir : {sudah_memilih} mahasiswa")
    print(f"Jumlah Pasukan Golput   : {golput} mahasiswa ({persentase_golput:.2f}%)")
    print(f"Grafik Partisipasi      : [{bar_visual}] {persentase_hadir:.2f}%")
    print("-" * 50)
    
    print("PEROLEHAN SUARA & KANDIDAT UNGGUL:")
    
    if not daftar_calon:
        print("   Belum ada data calon ketua di sistem.")
        return
        
    for c in daftar_calon:
        if sudah_memilih > 0:
            persentase_suara = (c["jumlah_suara"] / sudah_memilih) * 100
        else:
            persentase_suara = 0.0
            
        skala_calon = int(persentase_suara // 10)
        bar_calon = "■" * skala_calon + "□" * (10 - skala_calon)
        print(f"   [{c['id']}] {c['nama']:<15} : {c['jumlah_suara']} suara [{bar_calon}] ({persentase_suara:.1f}%)")
        
    print("-" * 50)
    
    suara_tertinggi = -1
    kandidat_pemenang = []
    
    for c in daftar_calon:
        if c["jumlah_suara"] > suara_tertinggi:
            suara_tertinggi = c["jumlah_suara"]
            
    for c in daftar_calon:
        if c["jumlah_suara"] == suara_tertinggi:
            kandidat_pemenang.append(c)
            
    if suara_tertinggi == 0 and sudah_memilih == 0:
        print("STATUS: Belum ada suara yang masuk ke sistem database.")
    else:
        if len(kandidat_pemenang) > 1:
            print("STATUS HASIL: PEMILU SERI / DRAW! (Butuh Pemilihan Ulang Antara Calon):")
            for pemenang in kandidat_pemenang:
                print(f"   {pemenang['nama']} ({pemenang['id']})")
        else:
            pemenang_tunggal = kandidat_pemenang[0]
            print(f"👑 PEMENANG UTAMA: {pemenang_tunggal['nama']} ({pemenang_tunggal['id']}) MENANG MUTLAK!")