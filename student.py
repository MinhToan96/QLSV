import os
import platform
import csv
import time
from prettytable import from_csv
import header_design as design
import main
import preloader

tab = '\t'
operating_system = platform.system()


def id_generator():
    id_list = []
    default_student_id = 1001
    try:
        with open('student_database.csv', 'r',encoding="utf-8") as fr:
            data = csv.reader(fr)
            for student_id in data:
                id_list.append(student_id[0])
            student_id = int(id_list[-1]) + 1
            return student_id
    except Exception:
        return default_student_id


# Adding New Student
def student_input():
    if operating_system == 'Linux':
        os.system('clear')
    elif operating_system == 'Windows':
        os.system('cls')

    design.art('Danh Sách Học Viên Học Chứng Chỉ CNTT Cơ Bản')
    student_id = id_generator()
    first_name = input('[+] Họ: ')
    middle_name = input('[+] Họ Đệm: ')
    last_name = input('[+] Tên: ')
    age = input('[+] Năm Sinh: ')
    gender = input('[+] Giới Tính: ')
    department = input('[+] Nhóm: ')

    while True:
        confirm = input('\n[!] Lưu lại? (y/n): ').lower()
        if confirm == 'y':
            if middle_name:
                name = first_name + ' ' + middle_name + ' ' + last_name

                # Saving information
                with open('student_database.csv', 'a', newline='', encoding="utf-8") as fs:
                    data = csv.writer(fs)
                    data.writerow([student_id, name, age, gender, department])
            else:
                name = first_name + ' ' + last_name

                # Saving information
                with open('student_database.csv', 'a', newline='', encoding="utf-8") as fs:
                    data = csv.writer(fs)
                    data.writerow([student_id, name, age, gender, department])
            print()

            msg = '[!] Vui lòng chờ! \n\n' + tab * 4 + 'Đang lưu'
            for i in range(5):
                preloader.load(msg)
            print('\n[✔] Đã Lưu')
            time.sleep(.5)

            main.StartMain.main(self='self')
            break
        elif confirm == 'n':
            print()
            msg = tab * 4 + '[!] Vui lòng chờ!'
            for i in range(5):
                preloader.load(msg)
            time.sleep(.5)
            main.StartMain.main(self='self')
            break
        else:
            print()
            print('[X] Vui lòng nhập đúng!')
            time.sleep(.50)


# Show student database
def student_database():
    if operating_system == 'Linux':
        os.system('clear')
    elif operating_system == 'Windows':
        os.system('cls')
    design.art('Student Database')

    try:
        with open('student_database.csv', 'r', encoding="utf-8") as fr:
            data_table = from_csv(fr, field_names=['ID', 'Họ & Tên', 'Tuổi', 'Giới Tính', 'Nhóm'])

        # Show student database
        print(data_table)
    except Exception as e:
        print(e)
        print('\nKhông tìm thấy. Vui lòng kiểm tra lại hoặc thêm học viên mới!\n')

    choice = input('\nNhập sự lựa chọn:\n'
                   '[1] Menu Chính\n'
                   '\n'
                   'admin@sms:~$ ')

    if choice == '1':
        main.StartMain.main(self='self')
    else:
        print()
        print('[X] Vui lòng nhập đúng!')
        time.sleep(.50)
        if operating_system == 'Linux':
            os.system('clear')
        elif operating_system == 'Windows':
            os.system('cls')
        student_database()


def search_student(search='id'):
    if search == 'id':
        print('[1] Tìm theo ID')
    elif search == 'first_name':
        print('[2] Tìm theo tên')


def search():
    if operating_system == 'Linux':
        os.system('clear')
    elif operating_system == 'Windows':
        os.system('cls')

    choice = input('Nhập sự lựa chọn:\n'
                   '[1] Tìm theo ID\n'
                   '[2] Tìm theo tên\n'
                   '[3] Trở lại\n'
                   '\n'
                   'admin@sms:~$ ')
    if choice is '1':
        search_student(search='id')
    elif choice is '2':
        search_student(search='first_name')
    elif choice is '3':
        pass
    else:
        print()
        print('[X] Vui lòng nhập đúng!')
        time.sleep(.50)
        search()
