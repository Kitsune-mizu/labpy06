data_mahasiswa = []

def tambah():
    data_mahasiswa.append({
        "nama": input("Masukkan nama mahasiswa: "),
        "nilai": float(input("Masukkan nilai mahasiswa: "))
    })
    print("Data berhasil ditambahkan!\n")

def tampilkan():
    if not data_mahasiswa:
        print("Tidak ada data.\n")
    else:
        print("Daftar Nilai Mahasiswa:")
        for i, mhs in enumerate(data_mahasiswa, 1):
            print(f"{i}. Nama: {mhs['nama']}, Nilai: {mhs['nilai']}")
        print()

def hapus(nama):
    for i, mhs in enumerate(data_mahasiswa):
        if mhs["nama"] == nama:
            data_mahasiswa.pop(i)
            print(f"Data {nama} berhasil dihapus!\n")
            return
    print(f"Data {nama} tidak ditemukan.\n")

def ubah(nama):
    for mhs in data_mahasiswa:
        if mhs["nama"] == nama:
            mhs["nilai"] = float(input(f"Masukkan nilai baru untuk {nama}: "))
            print(f"Data {nama} berhasil diubah!\n")
            return
    print(f"Data {nama} tidak ditemukan.\n")

while True:
    print("Menu:\n1. Tambah data\n2. Tampilkan data\n3. Hapus data\n4. Ubah data\n5. Keluar")
    pilihan = input("Pilih menu (1-5): ")
    if pilihan == "1":
        tambah()
    elif pilihan == "2":
        tampilkan()
    elif pilihan == "3":
        hapus(input("Masukkan nama mahasiswa yang ingin dihapus: "))
    elif pilihan == "4":
        ubah(input("Masukkan nama mahasiswa yang ingin diubah: "))
    elif pilihan == "5":
        print("Program selesai. Terima kasih!")
        break
    else:
        print("Pilihan tidak valid. Silakan coba lagi.\n")
