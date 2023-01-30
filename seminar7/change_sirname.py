import json
import controller

phone_number = 'phone_number .json'


def change_surname():
    name = input('Введите имя или фамилию контакта:  ') #у него будет меняться фамилия

    with open(phone_number, 'r', encoding='UTF-8') as file:
        data = json.load(file)
        for i in range(0, len(data)):
            if name == data[i]['Фамилия'] or name == data[i]['Фамилия']:
                data[i]['Фамилия'] = input('Новая фамилия: ')
    with open(phone_number, 'w', encoding='UTF-8') as file:
        json.dump(data, file, indent=4)
    print('\nФамилия  изменена\n')
    controller.user_choice()