from push_inf import *
from export_information import *
from print_information import *
from search_information import *


def greeting():
    print("Добро пожаловать в информационную систему  учеников!")

def start():
    print("Доступные операции:\n\
    1 - получить всю информацию о учениках;\n\
    2 - добавить ученика;\n\
    3 - поиск ученика;\n\
    4 - выход.")
    ch = input("Введите цифру: ")
    while True:
        if ch == '1':
            data = export_information()
            print_information(data)
            start()
        elif ch == '2':
            push_inf()
            start()
        elif ch == '3':
            info = input("Введите данные для поиска: ")
            data = export_information()
            item = search_information(info, data)
            if item != None:
                print_information(item, True)
            else:
                print("Данные не обнаружены")                
            start()
        elif ch == '4':
            print("выход")
            break
        else:
            print("Введите корректную цифру!")
            start()