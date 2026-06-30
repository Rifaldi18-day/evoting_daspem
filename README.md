# Sistem E-Voting Pemilihan Ketua Organisasi Mahasiswa

Proyek ini merupakan simulasi sistem e-voting sederhana berbasis CLI menggunakan Python. Mahasiswa dapat memilih calon ketua organisasi dan melihat hasil pemilu secara real-time.

## Fitur Utama
- Input dan manajemen data pemilih (Registrasi otomatis dengan Auto-Increment ID `PMxxx`)
- Input dan manajemen data calon (Pembuatan ID otomatis `CLxxx` via Panel Admin)
- Perbedaan menu akses (Multi-role) antara pemilih dan admin
- Proses voting dengan validasi ketat satu suara per pemilih (Anti-double voting)
- Statistik pemilu sederhana secara real-time

## Struktur Folder
```
e_voting/
├── main.py
├── modul/
│   ├── pemilih.py
│   ├── calon.py
│   ├── voting.py
│   ├── statistik.py
│   └── utils.py
├── data/
│   ├── pemilih.json
│   └── calon.json
└── README.md
```

## Cara Menjalankan
1. Clone repositori ini ke penyimpanan lokal komputer/laptop.
2. Pastikan Python 3 sudah terinstal, lalu jalankan file `main.py`.
3. Ikuti alur menu navigasi CLI untuk registrasi, voting, maupun mengelola data.

## Dibuat oleh:
- Adam Rifaldi
- 20250040134
- TI25