from modul import pemilih, calon, voting, statistik

def main():
    while True:
        print("\n===== SISTEM E-VOTING =====")
        print("1. Daftar Pemilih")
        print("2. Daftar Calon Ketua")
        print("3. Voting")
        print("4. Tampilkan Hasil Sementara")
        print("5. Statistik Pemilu")
        print("6. Keluar")

        pilihan = input("Pilih menu (1-6): ")

        if pilihan == "1":
            pemilih.tambah_pemilih()
        elif pilihan == "2":
            calon.tambah_calon()
        elif pilihan == "3":
            voting.lakukan_voting()
        elif pilihan == "4":
            voting.tampilkan_hasil()
        elif pilihan == "5":
            statistik.tampilkan_statistik()
        elif pilihan == "6":
            print("Terima kasih!")
            break
        else:
            print("Pilihan tidak valid.")

if __name__ == "__main__":
    main()