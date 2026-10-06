import json

def baca_data():
    with open("json/NilaiMahasiswa.json", "r", ) as f:
        data = json.load(f)
    return data

def tampilkan_data():
    data = baca_data()
    
    print("\n===== Data Nilai Mahasiswa =====")

    if data == []:
        print("Belum ada data nilai.")
    else:
        for mahasiswa in data:
            print("Nama     :", mahasiswa["Nama"])
            print("NIM      :", mahasiswa["NIM"])
            print("Mata Kuliah:", mahasiswa["Mata Kuliah"])
            print("Nilai    :", mahasiswa["Nilai"])
            print("------------------------")

def tambah_data():
    data = baca_data()

    print("\n===== Tambah Data Nilai Mahasiswa =====")

    nama = input("Nama     : ")
    nim = input("NIM      : ")
    mata_kuliah = input("Mata Kuliah: ")    
    nilai = int(input("Nilai    : "))

    data_baru = {
        "Nama": nama,
        "NIM": nim,
        "Mata Kuliah": mata_kuliah,
        "Nilai": nilai
    }

    data.append(data_baru)

    with open("json/NilaiMahasiswa.json", "w") as f:
        json.dump(data, f, indent=4)

    print("Data nilai berhasil ditambahkan.")

while True:
    print("\n===== SISTEM PENCATATAN NILAI MAHASISWA =====")
    print("1. Lihat Data Nilai")
    print("2. Tambah Data Nilai")
    print("3. Keluar")

    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        tampilkan_data()
    elif pilihan == "2":
        tambah_data()
    elif pilihan == "3":
        print("Program selesai.")
        break

    else:
        print("Pilihan tidak tersedia.")