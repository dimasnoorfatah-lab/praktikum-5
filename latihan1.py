data_nilai = {}   # Dictionary untuk menyimpan data mahasiswa

def hitung_nilai_akhir(tugas, uts, uas):
    return (0.30 * tugas) + (0.35 * uts) + (0.35 * uas)

while True:
    print("\n=== MENU PILIHAN ===")
    print("1. Tambah Data")
    print("2. Ubah Data")
    print("3. Hapus Data")
    print("4. Tampilkan Data")
    print("5. Cari Data")
    print("6. Keluar")

    pilih = input("Pilih menu (1-6): ")

    # ---------------- TAMBAH DATA ----------------
    if pilih == "1":
        nama = input("Masukkan nama mahasiswa: ")
        tugas = float(input("Nilai Tugas: "))
        uts = float(input("Nilai UTS : "))
        uas = float(input("Nilai UAS : "))

        nilai_akhir = hitung_nilai_akhir(tugas, uts, uas)
        data_nilai[nama] = {
            "tugas": tugas,
            "uts": uts,
            "uas": uas,
            "akhir": nilai_akhir
        }
        print("Data berhasil ditambahkan!")

    # ---------------- UBAH DATA ----------------
    elif pilih == "2":
        nama = input("Masukkan nama yang akan diubah: ")
        if nama in data_nilai:
            tugas = float(input("Nilai Tugas baru: "))
            uts = float(input("Nilai UTS baru : "))
            uas = float(input("Nilai UAS baru : "))

            nilai_akhir = hitung_nilai_akhir(tugas, uts, uas)
            data_nilai[nama] = {
                "tugas": tugas,
                "uts": uts,
                "uas": uas,
                "akhir": nilai_akhir
            }
            print("Data berhasil diubah!")
        else:
            print("Data tidak ditemukan!")

    # ---------------- HAPUS DATA ----------------
    elif pilih == "3":
        nama = input("Masukkan nama yang akan dihapus: ")
        if nama in data_nilai:
            del data_nilai[nama]
            print("Data berhasil dihapus!")
        else:
            print("Data tidak ditemukan!")

    # ---------------- TAMPILKAN DATA ----------------
    elif pilih == "4":
        print("\n=== DAFTAR DATA NILAI ===")
        if not data_nilai:
            print("Belum ada data.")
        else:
            for nama, nilai in data_nilai.items():
                print(f"Nama : {nama}")
                print(f"  Tugas : {nilai['tugas']}")
                print(f"  UTS   : {nilai['uts']}")
                print(f"  UAS   : {nilai['uas']}")
                print(f"  Nilai Akhir : {nilai['akhir']:.2f}")
                print("-"*30)

    # ---------------- CARI DATA ----------------
    elif pilih == "5":
        nama = input("Masukkan nama yang dicari: ")
        if nama in data_nilai:
            nilai = data_nilai[nama]
            print(f"\nData ditemukan untuk {nama}:")
            print(f"  Tugas : {nilai['tugas']}")
            print(f"  UTS   : {nilai['uts']}")
            print(f"  UAS   : {nilai['uas']}")
            print(f"  Nilai Akhir : {nilai['akhir']:.2f}")
        else:
            print("Data tidak ditemukan!")

    # ---------------- KELUAR ----------------
    elif pilih == "6":
        print("Program selesai. Terima kasih!")
        break

    else:
        print("Pilihan tidak valid, coba lagi!") 
