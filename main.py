import sys
import time
import os
import platform
import header_design as design
import student as st
import preloader

tab = '\t'
operating_system = platform.system()


class StartMain:

    # Main Function
    @staticmethod
    def main(self):
        if operating_system == 'Linux':
            os.system('clear')
        elif operating_system == 'Windows':
            os.system('cls')

        design.art('Danh Sách Học Viên Học Chứng Chỉ CNTT Cơ Bản')

        choice = input('Nhập sự lựa chọn:\n'
                       '[1] Thêm học viên mới\n'
                       '[2] Danh sách học viên\n'
                       '[3] Tìm Học Viên\n'
                       '[4] Thoát\n'
                       '\n'
                       'admin@sms:~$ ')
        if choice is '1':
            st.student_input()
        elif choice == '2':
            st.student_database()
        elif choice is '3':
            st.search_student()
        elif choice is '4':
            print()

            msg = '[☺] Hẹn gặp lại!\n\n' + tab * 4 + 'Thoát'
            for i in range(3):
                preloader.load(msg)
            time.sleep(1)
            sys.exit()
        else:
            print()
            print('[✘] Vui lòng nhập đúng!')
            time.sleep(.50)
            StartMain().main(self)
