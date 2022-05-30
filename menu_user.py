import os

class buat_post():
    def __init__(self,pilihan):
        self.pil = pilihan

    def menu(self):
        if self.pil == 1:
            from inputBarang import input_data_lost
            input_data_lost()

        elif self.pil == 2:
            from inputBarang import input_data_found
            input_data_found()

        elif self.pil == 3:
            os.system("cls")
            mainnn()

        else:
            os.system("cls")
            print("Menu Tidak Tersedia")
            cho = input("Kembali Ke Main Menu ? (y/t) : ")
            if cho == 'y':
                os.system("cls")
                mainnn()
            else :
                os.system("pause")
            

class lihat_post():
    def __init__(self,pilihan):
        self.pil1 = pilihan

    def menu(self):
        if self.pil1 == 1:
            os.system("cls")
            from lihatsemuaBarang import lihat_semua_barang
            x = lihat_semua_barang()
            x.listbarang()

        elif self.pil1 == 2:
            os.system('cls')
            from cariBarang import mainn
            mainn()

        elif self.pil1 == 3:
            os.system("cls")
            mainnn()

        else:
            os.system("cls")
            print("Menu Tidak Tersedia")
            ch = input("Kembali Ke Main Menu ? (y/t) : ")
            if ch == 'y':
                os.system("cls")
                mainnn()
            else :
                os.system("pause")

def mainnn():
    print("\n[MAIN MENU]\n")
    print("1. Buat Post")
    print("2. Lihat Post")
    print("3. Konfirmasi Barang")

    pil = int(input("Masukkan : "))
    if pil == 1:
        os.system('cls')
        print("\n[MENU BUAT POST]\n")
        print("1. Post Kehilangan Barang")
        print("2. Post Penemuan Barang")
        print("3. Kembali")
        i = int(input("Masukkan Pilihan : "))
        x = buat_post(i)
        x.menu()

    elif pil == 2:
        os.system('cls')
        print("\n[MENU LIHAT POST]\n")
        print("1. Lihat Daftar Barang")
        print("2. Cari Daftar Barang")
        print("3. Kembali")
        j = int(input("Masukkan Pilihan : "))
        y = lihat_post(j)
        y.menu()

    elif pil == 3:
        from konfirmasiBarang import menu_konfirmasi
        menu_konfirmasi()


    else:
        print("Menu Tidak Tersedia")
        os.system("pause")
        os.system("cls")
        mainnn()

mainnn()
