import os
class konfirmasiLost():
    def __init__(self,nama,namapenemu,id_brg):
        self.nama = nama
        self.namapenemu = namapenemu
        self.kode = id_brg

    def sudah_diambil(self):
        file = open("konfirmasiLost.txt","a")
        file.write("{}#{}#{}#\n".format(self.kode,self.nama,self.namapenemu))
        print("\n[ Info Berhasil di Tambahkan ] ")
        file.close()
        os.system("pause")
        menu_konfirmasi()

class konfirmasiFound(konfirmasiLost):
    def __init__(self,nama,namapenemu,id_brg):
        super().__init__(nama,namapenemu,id_brg)

    def sudah_ditemukan(self):
        file = open("konfirmasiFound.txt", "a")
        file.write("{}#{}#{}#\n".format(self.kode, self.nama, self.namapenemu))
        print("\n[ Info Berhasil di Tambahkan ] ")
        file.close()
        os.system("pause")
        menu_konfirmasi()

def menu_konfirmasi():
    os.system("cls")
    print("[ KONFIRMASI ]")

    print("1. Konfirmasi Barang Sudah DiAmbil")
    print("2. Konfirmasi Barang Sudah DiKembalikan")
    print("3. Kembali")

    m = int(input("Masukkan Pilihan : "))

    if m == 1:
        os.system("cls")
        id = int(input("Masukkan ID dari Penemu : "))
        nama = input("Masukkan Nama Anda      : ")
        namatemu = input("Masukkan Nama Penemu    : ")
        confirm = konfirmasiLost(nama, namatemu, id)
        confirm.sudah_diambil()

    elif m == 2:
        os.system("cls")
        id = int(input("Masukkan ID Kehilangan          : "))
        nama = input("Masukkan Nama Anda              : ")
        namatemu = input("Masukkan Nama Pemilik Barang    : ")
        confirm2 = konfirmasiFound(nama, namatemu, id)
        confirm2.sudah_ditemukan()

    elif m == 3:
        os.system("cls")
        from menu_user import mainnn
        mainnn()
        