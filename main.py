import os
from LoginRegister_User import login


class homepage(login):

    def __init__(self,pilihan):
        self.pilih = pilihan

    def login_daftar(self):

        if (self.pilih == 1):
            login.input_register(self)

        elif (self.pilih == 2):
            login.input_login(self)

        else:
            os.system('cls')
            print("Pilihan Tidak Tersedia")
            os.system("pause")

print("\n[WELCOME]\n")
print("1. Sign Up")
print("2. Sign In\n")
pil = int(input("Pilih (1/2): "))

x = homepage(pil)
x.login_daftar()



