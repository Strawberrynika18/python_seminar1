import json
import controller


phone_number = 'phone_number.json'


def change_phone_number():  
    name = input('Введите имя или фамилию контакта, чей номер будем менять:  ')
   
    with open(phone_number, 'r', encoding='UTF-8') as file:
        data = json.load(file)
        for i in range(0, len(data)):  
            if name == data[i]['Имя'] or name == data[i]['Фамилия']:
                data[i]['Номер телефона'] = input('Новый телефон: ')
  
    with open(phone_number, 'w', encoding='UTF-8') as file:
        json.dump(data, file, indent=4)
    print('\nНомер  изменён\n')
    controller.user_choice()