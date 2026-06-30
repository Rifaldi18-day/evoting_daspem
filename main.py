from modul import pemilih, calon, voting, statistik

def main():
    while True:
        print("\n===== SELAMAT DATANG DI SISTEM E-VOTING =====")
        print("ANDA MASUK SEBAGAI ADMIN ATAU PEMILIH?")
        print("1. pemilih")
        print("2. Admin")
        print("3. Keluar Aplikasi")
        
        peran = input("Pilih akses (1-3): ").strip()
        if peran == "1":
            while True:
                print("\n--- PANEL UTAMA PEMILIH ---")
                print("1. Registrasi Mandiri")
                print("2. Lakukan Voting")
                print("3. Kembali ke Menu Utama")
                
                pilihan_pemilih = input("Pilih menu Pemilih (1-3): ").strip()
                
                if pilihan_pemilih == "1":
                    pemilih.tambah_pemilih()
                elif pilihan_pemilih == "2":
                    voting.lakukan_voting()
                elif pilihan_pemilih == "3":
                    print("Kembali ke menu utama...")
                    break
                else:
                    print("Pilihan tidak valid.")
                    
        elif peran == "2":
            password = input("Masukkan Password Admin: ")
            if password == "RIPAL123":
                print("LOGIN ADMIN BERHASIL!")
                while True:
                    print("\n--- PANEL UTAMA ADMIN (RAHASIA) ---")
                    print("1. Pendaftaran Data Calon Ketua")
                    print("2. Tampilkan Perolehan Suara Sementara")
                    print("3. Analisis Statistik Pemilu")
                    print("4. Keluar/Log Out dari Admin")
                    
                    pilihan_admin = input("Pilih menu Admin (1-4): ").strip()
                    
                    if pilihan_admin == "1":
                        calon.tambah_calon()
                    elif pilihan_admin == "2":
                        voting.tampilkan_hasil()
                    elif pilihan_admin == "3":
                        statistik.tampilkan_statistik()
                    elif pilihan_admin == "4":
                        print("Keluar dari panel admin...")
                        break
                    else:
                        print("Pilihan tidak valid.")
            else:
                print("GAGAL: Password Admin Salah! Akses Ditolak.")
                

        elif peran == "3":
            print("Terima kasih telah menggunakan Sistem E-Voting. Sampai jumpa!")
            break
        else:
            print("Pilihan tidak valid.")
#
if __name__ == "__main__":
    main()