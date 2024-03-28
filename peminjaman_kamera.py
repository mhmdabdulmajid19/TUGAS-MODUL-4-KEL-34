from method import Metode

print("Selamat datang di Program Peminjaman Kamera\n")

def listKamera():
    print("""Daftar kamera yang tersedia:
1 : Canon EOS R       - Rp. 200.000
2 : Sony Alpha A7 III - Rp. 150.000
3 : Nikon Z6          - Rp. 170.000
4 : Fujifilm X-T4     - Rp. 140.000
5 : Panasonic Lumix GH5 - Rp. 160.000
0 : Batal""")

def opsiKamera(opsi):
    switcher = {
        1: "Canon EOS R",
        2: "Sony Alpha A7 III",
        3: "Nikon Z6",
        4: "Fujifilm X-T4",
        5: "Panasonic Lumix GH5",
        0: "Keluar dari program",
    }
    return switcher.get(opsi, "Pilihan tidak valid")

def hargaKamera(opsi):
    switcher = {
        1: 200000,
        2: 150000,
        3: 170000,
        4: 140000,
        5: 160000,
    }
    return switcher.get(opsi, 0)
    
def peminjamanKamera():
    total_harga = 0
    while True:
        listKamera()
        opsi = int(input("Pilih kamera yang ingin dipinjam (masukkan nomor): "))
        if opsi == 0:
            break
        print("Anda telah memilih kamera:", opsiKamera(opsi))
        hari = int(input("Berapa hari Anda ingin meminjam kamera ini? "))
        harga_per_hari = hargaKamera(opsi)
        total_harga += harga_per_hari * hari
        lanjut = input("Apakah Anda ingin meminjam kamera lain? (ya/tidak): ")
        if lanjut.lower() != "ya":
            break
    return total_harga


panggil = Metode(None)

total_harga_peminjaman = peminjamanKamera()
print("Total harga peminjaman kamera: Rp.", total_harga_peminjaman)

panggil.trims()

input("Tekan ENTER untuk keluar dari program")
