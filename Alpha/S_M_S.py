import time
import os
import getpass
import sys
import csv
from prettytable import from_csv


class StudentInfo:

    @staticmethod
    def welcome_banner():
        print('''                        
                        #########################################################
                        ##### Danh Sách Học Viên Học Chứng Chỉ CNTT Cơ Bản  #####
                        #########################################################
            ''')

    @staticmethod
    def design(function_name='Default'):
        print('                    ######################################')
        print('                        ######## ' + function_name + ' #########')
        print('                    ######################################')

    @staticmethod
    def loader(string='###LOADING...###'):
        os.system('clear')
        print('\n\n\n\n\n\n')
        for char in string:
            print(char, end='')
            sys.stdout.flush()
            time.sleep(0.02)
        print()

    # Login System as Admin
    def authentication(self):
        os.system('clear')
        self.design('Trang Đăng Nhập')
        print('Vui lòng mật khẩu')
        password = getpass.getpass()

        chance = 3

        if password == 'password':
            print('\nLogin In...')
            time.sleep(1)
            self.loader('Loading...#######################################..Complete')
            self.main()
        else:
            while password != 'password':
                chance -= 1
                if chance != 0:
                    print('Sai mật khẩu!. Bạn còn ' + str(chance) + ' cơ hội')
                    password = getpass.getpass()
                    if password == 'password':
                        print('\nĐăng Nhập...')
                        time.sleep(1)
                        self.loader('Loading...#######################################...Complete')
                        self.main()
                else:
                    print('\nSai mật khẩu!')
                    print('Thoát...')
                    time.sleep(2)
                    sys.exit()

    @staticmethod
    def id_generator():
        id_list = []
        default_student_id = 1001
        try:
            with open('student_database.csv', 'r', encoding="utf-8") as fr:
                data = csv.reader(fr)
                for student_id in data:
                    id_list.append(student_id[0])
                student_id = int(id_list[-1]) + 1
                return student_id
        except Exception:
            return default_student_id

    # Adding New Student
    def student_input(self):
        os.system('clear')
        self.design('Thêm học viên mới')
        student_id = self.id_generator()
        first_name = input('Họ: ')
        middle_name = input('Họ Đệm: ')
        last_name = input('Tên: ')
        age = input('Tuổi: ')
        gender = input('Giới Tính: ')

        while True:
            confirm = input('\nLưu lại? (y/n): ').lower()
            if confirm == 'y':
                if middle_name:
                    name = first_name + ' ' + middle_name + ' ' + last_name

                    # Saving information
                    with open('student_database.csv', 'a', encoding="utf-8") as fs:
                        data = csv.writer(fs)
                        data.writerow([student_id, name, age, gender])
                else:
                    name = first_name + ' ' + last_name

                    # Saving information
                    with open('student_database.csv', 'a', encoding="utf-8") as fs:
                        data = csv.writer(fs)
                        data.writerow([student_id, name, age, gender])
                print()
                print('Đang lưu...')
                time.sleep(.5)
                self.main()
                break
            elif confirm == 'n':
                print()
                print('Đang trở về menu chính...')
                time.sleep(.5)
                self.main()
                break
            else:
                print()
                print('[X] Vui lòng nhập đúng!')
                time.sleep(.50)

    # Show student database
    def student_database(self):
        os.system('clear')
        self.design('Danh Sách Học Viên')

        try:
            with open('student_database.csv', 'r', encoding="utf-8") as fr:
                data_table = from_csv(fr, field_names=['Student ID', 'Student Name', 'Age', 'Gender'])

            # Show student database
            print(data_table)
        except Exception:
            print('\nKhông tìm thấy. Vui long kiểm tra hoặc nhập mới!.\n')

        choice = input('\nNhập sự lựa chọn:\n'
                       '[1] Menu chính\n')
        if choice == '1':
            self.main()
        else:
            print()
            print('[X] Vui lòng nhập đúng!')
            self.student_database()

    @staticmethod
    def search_student(search='id'):
        if search == 'id':
            print('Tìm theo ID')
        elif search == 'first_name':
            print('Tìm kiếm theo tên')

    def search(self):
        os.system('clear')
        self.design('Search')

        choice = input('Nhập sự lựa chọn:\n'
                       '[1] Tìm theo ID\n'
                       '[2] Tìm theo tên\n'
                       '[3] Trở lại\n')
        if choice is '1':
            self.search_student(search='id')
        elif choice is '2':
            self.search_student(search='first_name')
        elif choice is '3':
            self.main()
        else:
            print()
            print('[X] Vui lòng nhập đúng!')
            time.sleep(.50)
            self.search()

    # Main Function
    def main(self):
        os.system('clear')
        self.welcome_banner()

        choice = input('Nhập sự lựa chọn:\n'
                       '[1] Thêm học viên mới\n'
                       '[2] Danh sách học viên\n'
                       '[3] Tìm Học Viên\n'
                       '[4] Thoát\n')
        if choice is '1':
            self.student_input()
        elif choice == '2':
            self.student_database()
        elif choice is '3':
            self.search()
        elif choice is '4':
            print()
            print('Hẹn gặp lại!')
            print('Thoát...')
            time.sleep(1)
            sys.exit()
        else:
            print()
            print('[X] Vui lòng nhập đúng!')
            time.sleep(.50)
            self.main()


if __name__ == '__main__':
    si = StudentInfo()
    si.authentication()
