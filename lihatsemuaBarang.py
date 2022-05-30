import os

class lihat_semua_barang:

    def listbarang(self):
        n = 0
        self.f = open("DaftarBarang.txt", "r")
        statusbrg = '\n[ Maaf, Jenis/Nama Barang Tidak Ditemukan ]'

        for row in self.f:
            index = row.split("#")

            kode = index[0]
            namabrg2 = index[3]  # INDEX KE- DLM TXT
            penemu = index[1]
            notelp = index[2]
            warna = index[4]
            detail_barang = index[5]
            detail_alamat = index[6]
            desa = index[7]
            kecamatan = index[8]
            kabupaten = index[9]
            keterangan = index[10]

            statusbrg = ' '
            n += 1
            print("\n-----------------------------------------------------------------------------------------")
            print("Data Ke - {} , {}".format(n, keterangan))
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
            file3 = open("konfirmasiFound.txt","r")
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

        print(statusbrg)
        self.f.close()
        lihat_semua_barang.back(self)

    def back(self):
        self.pil = input("\n\nKembali Ke Menu Utama ? (y/t) : ")
        if self.pil == 'y':
            os.system('cls')  #close, keliatan kalo run di cmd kalo di teks editor ga keliatan
            from menu_user import mainnn
            mainnn()
        else :
            exit()


