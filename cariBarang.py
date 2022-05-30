import os

class CariBarang:
    def __init__(self,namabrg,alamathlg):
        self.namabrg = namabrg
        self.alamat_hlg = alamathlg

    def cari_berdasarkan_nama(self):
        n = 0
        self.f = open("DaftarBarang.txt","r")
        statusbrg = '\n[ Maaf, Jenis/Nama Barang Tidak Ditemukan ]'

        for row in self.f:
            index = row.split("#")

            kode = index[0]
            namabrg2 = index[3]
            penemu = index[1]
            notelp = index[2]
            warna = index[4]
            detail_barang = index[5]
            detail_alamat = index[6]
            desa = index[7]
            kecamatan = index[8]
            kabupaten = index[9]
            keterangan = index[10]

            if self.namabrg == namabrg2:
                statusbrg = ' '
                n += 1
                print("\n-----------------------------------------------------------------------------------------")
                print("Data Ke - {} , {}".format(n,keterangan))
                print("-----------------------------------------------------------------------------------------")
                print("[ Detail Barang ]")
                print("Nama Pelapor        : {} ".format(penemu))
                print("Nama Barang         : {} ".format(namabrg2))
                print("Warna Barang        : {} ".format(warna))
                print("Detail Barang       : {} ".format(detail_barang))
                print("\n[ Detail Lokasi Penemuan/Kehilangan ]")
                print("Desa/Kelurahan      : {} ".format(desa))
                print("Kecamatan           : {} ".format(kecamatan))
                print("Kabupaten           : {} ".format(kabupaten))
                print("Detail Lokasi       : {} ".format(detail_alamat))
                print("\n[ Anda Dapat menghubungi Nomor : 0{} Untuk Mengambil Barang ]".format(notelp))

                file2 = open("konfirmasiLost.txt", "r")
                status = 'Belum Diambil Pemilik'

                file2 = open("konfirmasiLost.txt", "r")
                file3 = open("konfirmasiFound.txt", "r")
                status = 'Belum Diambil Pemilik / Belum Dikembalikan'

                for baris in file3:
                    index3 = baris.split("#")

                    idkonfirmasi = index3[0]

                    if kode == idkonfirmasi:
                        status = 'Sudah DiKembalikan'
                    else:
                        continue

                for baris in file2:
                    index2 = baris.split("#")

                    idkonfirmasi = index2[0]

                    if kode == idkonfirmasi:
                        status = 'Sudah Diambil Pemilik'
                    else:
                        continue
                print("Status Barang : {}".format(status))

            else:
                continue
        
        print(statusbrg)
        self.f.close()
        CariBarang.back(self)

    def cari_berdasarkan_alamat(self):
        n = 0
        self.f = open("DaftarBarang.txt", "r")
        statusbrg2 = '\n[ Maaf , Alamat Tidak Ditemukan ]'

        for row in self.f:
            index = row.split("#")

            kode = index[0]
            namabrg2 = index[3]
            penemu = index[1]
            notelp = index[2]
            warna = index[4]
            detail_barang = index[5]
            detail_alamat = index[6]
            desa = index[7]
            kecamatan = index[8]
            kabupaten = index[9]
            keterangan = index[10]

            if self.alamat_hlg == desa:
                statusbrg2 = ' '
                n += 1
                print("\n-----------------------------------------------------------------------------------------")
                print("Data Ke - {} , {}".format(n,keterangan))
                print("-----------------------------------------------------------------------------------------")
                print("[ Detail Barang ]")
                print("Nama Pelapor        : {} ".format(penemu))
                print("Nama Barang         : {} ".format(namabrg2))
                print("Warna Barang        : {} ".format(warna))
                print("Detail Barang       : {} ".format(detail_barang))
                print("\n[ Detail Lokasi Penemuan/Kehilangan ]")
                print("Desa/Kelurahan      : {} ".format(desa))
                print("Kecamatan           : {} ".format(kecamatan))
                print("Kabupaten           : {} ".format(kabupaten))
                print("Detail Lokasi       : {} ".format(detail_alamat))
                print("\n[ Anda Dapat menghubungi Nomor : 0{} Untuk Mengambil Barang ]".format(notelp))

                file2 = open("konfirmasiLost.txt", "r")
                status = 'Belum Diambil Pemilik'

                for baris in file2:
                    index3 = baris.split("#")

                    idkonfirmasi = index3[0]

                    if kode == idkonfirmasi:
                        status = 'Sudah Diambil Pemilik'
                    else:
                        continue
                print("Status Barang : {}".format(status))

            else:
                continue

        print(statusbrg2)
        self.f.close()
        CariBarang.back(self)

    def back(self):
        self.pil = input("\n\nKembali Ke Pencarian ? (y/t) : ")
        if self.pil == 'y':
            os.system('cls')
            mainn()
        else:
            exit()


def mainn():
    print("\n[CARI DAFTAR BARANG]\n")
    print("1. Cari Berdasarkan Nama Barang")
    print("2. Cari Berdasarkan Lokasi Menemukan/Kehilangan")
    print("3. Kembali")
    p = int(input("Masukkan Pilihan : "))
    if p == 1:
        os.system("cls")
        namaBarang = input("Masukkan Nama Barang : ")
        cari = CariBarang(namaBarang," ")
        cari.cari_berdasarkan_nama()
    elif p == 2:
        os.system("cls")
        alamathilang = input("Masukkan Lokasi Menemukan/Kehilangan (Desa/Kelurahan) : ")
        cari2 = CariBarang(" ",alamathilang)
        cari2.cari_berdasarkan_alamat()
    elif p == 3:
        os.system("cls")
        from menu_user import mainnn
        mainnn()
    else:
        print("Pilihan Tidak Tersedia")
        
mainn()