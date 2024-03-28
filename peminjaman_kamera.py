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
