import getpass
import os
import platform
import sys
import time
import header_design
from main import StartMain
import preloader

tab = '\t'
operating_system = platform.system()


class Admin:

    # Login System as Admin
    def authentication(self):
        if operating_system == 'Linux':
            os.system('clear')
        elif operating_system == 'Windows':
            os.system('cls')

        header_design.art('Trang Đăng Nhập')
        print(tab + ' ' * 5 + '[!] Vui lòng đăng nhập vào hệ thống\n')
        print(tab * 3 + 'Username: admin')
        password = getpass.getpass(tab * 3 + 'Password: ')

        chance = 3
        if password == 'admin':

            msg = '[!] Đăng Nhập. \n\n' + tab * 4 + 'Vui lòng chờ...'
            for i in range(5):
                preloader.load(msg)

            time.sleep(.05)
            print('\n[!] Đăng nhập thành công')
            time.sleep(.5)
            if operating_system == 'Linux':
                os.system('clear')
            elif operating_system == 'Windows':
                os.system('cls')

            StartMain.main(self)

        else:
            while password != 'admin':
                chance -= 1

                if chance != 0:
                    print('[✘] Sai mật khẩu!. Bạn còn ' + str(chance) + ' cơ hội')
                    password = getpass.getpass()
                    if password == 'admin':

                        msg = '[!] Đăng nhập. \n\n' + tab * 4 + 'Vui lòng chờ...'
                        for i in range(5):
                            preloader.load(msg)

                        print('\n[✔] Đăng nhập thành công')
                        time.sleep(.5)
                        StartMain.main(self)

                else:
                    msg = '[✘] Thất bại!\n\n' + tab * 4 + 'Đang thoát...'
                    for i in range(5):
                        preloader.load(msg)
                    time.sleep(2)
                    sys.exit()
