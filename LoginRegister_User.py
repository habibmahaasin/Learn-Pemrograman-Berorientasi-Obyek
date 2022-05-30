import os
class login:
    def __init__(self):
        self.f = open("akun.txt")
        self.f.close()
    
    def simpan_data(self,username,password,notelp,j_kel):

        self.f = open("akun.txt",'a')
        self.username = username
        self.__password = password
        self.__notelp = notelp
        self.j_kel = j_kel
        self.f.write("{} {} {} {}\n".format(self.username,self.__password,self.__notelp,self.j_kel,))
        self.f.close()

        print("\nTerimakasih, Akun Berhasil Ditambahkan!\n")
        back = input("[ LANJUT KE HALAMAN LOGIN ? (y/t) ] : ")
        if back == 'y':
            login.input_login(self)
        else :
            os.system("pause")


    def cek_password(self,username,password):

        self.f = open("akun.txt",'r')
        self.isi = self.f.read()
        self.isi = self.isi.split()
        self.username = username
        self.password = password

        self.posisi = self.isi.index(username) + 1
        self.passuser = self.isi[self.posisi]
        if self.passuser == self.password:
            print ("\n[ Welcome back {} . Tekan Enter Untuk Masuk Kedalam Menu ] ".format(self.username))
            os.system("pause")
            os.system("cls")
            from menu_user import mainnn
            mainnn()

        else:
            print("\nPassword yang Anda Masukkan Salah!\n")
            os.system("pause")
            login.input_login(self)


    def input_register(self):
        os.system("cls")
        self.f = open("akun.txt", 'r')
        self.isi = self.f.read()

        print("\n[REGISTER PAGE]\n")

        self.username = input("Masukkan Username : ")

        if self.username in self.isi:
            print("\nNama Sudah Digunakan, Silahkan Coba Lagi!\n")
            os.system("pause")
            login.input_register(self)
        else:
            self.password = input("Masukkan Password : ")
            lenpw = len(self.password)

            if lenpw < 5:
                print("\nPassword yang anda masukkan Terlalu Pendek! (Min. 5 Karakter)\n")
                os.system("pause")
                login.input_register(self)
            else:
                self.notelp = int(input("Noomor Telp       : (+62) "))
                self.j_kel = input("Jenis Kel (L/P)   : ")

                login.simpan_data(self,self.username,self.password,self.notelp,self.j_kel)


    def input_login(self):
        os.system("cls")
        self.f = open("akun.txt", 'r')
        self.isi = self.f.read()

        print("\n[LOGIN PAGE]\n")

        self.username = input("Masukkan Username: ")
        if self.username in self.isi:
            self.password = input("Masukkan Password: ")
            login.cek_password(self,self.username, self.password)

        else:
            print("\nNama Tidak Ditemukan, Silahkan Masukkan Ulang\n")
            os.system("pause")
            login.input_login(self)
        self.f.close()

