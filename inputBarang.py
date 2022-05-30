import random
import os

class id_unik:

    def __init__(self,id):
        self.id = id

    def random_angka(self):
        self.id = random.randint(10000,9999999)

class data_barang_found(id_unik):

    def __init__(self,nama,notelp,jenis_barang,warna,detail_barang,posisi_lokasi,desa,kecamatan,kabupaten):
        super().__init__(self)
        self.keterangan = "Saya Menemukan Barang"
        self.nama = nama
        self.no = notelp
        self.jenis = jenis_barang
        self.warna = warna
        self.detail = detail_barang
        self.lokasi_lengkap = posisi_lokasi
        self.desa = desa
        self.kecamatan = kecamatan
        self.kabupaten = kabupaten

    def simpan_info(self):
        file = open("DaftarBarang.txt", "r")
        self.random_angka()

        if self.id in file:
            self.simpan_info()
        else:
            file = open("DaftarBarang.txt", "a")
            file.write("{}#{}#{}#{}#{}#{}#{}#{}#{}#{}#{}#\n".format(str(self.id),self.nama,self.no,self.jenis,self.warna,self.detail,self.lokasi_lengkap,self.desa,self.kecamatan,self.kabupaten,self.keterangan))
            print("\n    ID BARANG YANG ANDA TEMUKAN : {}".format(self.id))
            print("[!] INFORMASI BARANG BERHASIL DITAMBAHKAN! [!]")
        file.close()

class data_barang_lost(id_unik):

    def __init__(self,nama,notelp,jenis_barang,warna,detail_barang,posisi_lokasi,desa,kecamatan,kabupaten):
        super().__init__(self)
        self.keterangan = "Saya Kehilangan Barang"
        self.nama = nama
        self.no = notelp
        self.jenis = jenis_barang
        self.warna = warna
        self.detail = detail_barang
        self.lokasi_lengkap = posisi_lokasi
        self.desa = desa
        self.kecamatan = kecamatan
        self.kabupaten = kabupaten

    def simpan_info(self):
        file = open("DaftarBarang.txt", "r")
        self.random_angka()

        if self.id in file:
            self.simpan_info()
        else:
            file = open("DaftarBarang.txt", "a")
            file.write("{}#{}#{}#{}#{}#{}#{}#{}#{}#{}#{}#\n".format(str(self.id),self.nama,self.no,self.jenis,self.warna,self.detail,self.lokasi_lengkap,self.desa,self.kecamatan,self.kabupaten,self.keterangan))
            print("\n    ID KEHILANGAN ANDA : {}".format(self.id))
            print("[!] INFORMASI BARANG BERHASIL DITAMBAHKAN! [!]")
        file.close()

def input_data_found():
    os.system("cls")
    print("\n[FORM] - DATA DIRI DAN BARANG")
    nama          = input("Nama Anda                : ")
    notelp        = int(input("Nomor Telp               : (+62)  "))
    jenis_barang  = input("Jenis Barang             : ")
    warna         = input("Warna Barang             : ")
    detail_barang = input("Deskripsi Detail Barang  : ")
    print("\n[FORM] - LOKASI")
    posisi_lokasi = input("Detail Lokasi Menemukan : ")
    desa          = input("Desa                     : ")
    kecamatan     = input("Kecamatan                : ")
    kabupaten     = input("Kabupaten                : ")

    barang = data_barang_found(nama,notelp,jenis_barang,warna,detail_barang,posisi_lokasi,desa,kecamatan,kabupaten)
    barang.simpan_info()


    print("[!]    HARAP SIMPAN ID  BARANG TERSEBUT    [!]")
    print("Kembali Ke Menu Utama")
    os.system("pause")
    os.system("cls")
    from menu_user import mainnn
    mainnn()

def input_data_lost():
    os.system("cls")
    print("\n[FORM] - DATA DIRI DAN BARANG")
    nama = input("Nama Anda                : ")
    notelp = int(input("Nomor Telp               : (+62)  "))
    jenis_barang = input("Jenis Barang             : ")
    warna = input("Warna Barang             : ")
    detail_barang = input("Deskripsi Detail Barang  : ")
    print("\n[FORM] - LOKASI")
    posisi_lokasi = input("Detail Lokasi Kehilangan : ")
    desa = input("Desa                     : ")
    kecamatan = input("Kecamatan                : ")
    kabupaten = input("Kabupaten                : ")

    barang = data_barang_lost(nama, notelp, jenis_barang, warna, detail_barang, posisi_lokasi, desa, kecamatan,kabupaten)
    barang.simpan_info()

    print("[!]    HARAP SIMPAN ID  BARANG TERSEBUT    [!]")
    print("Kembali Ke Menu Utama")
    os.system("pause")
    os.system("cls")
    from menu_user import mainnn
    mainnn()

