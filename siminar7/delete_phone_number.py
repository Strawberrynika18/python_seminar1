import json
import controller


phone_number = 'phone_number.json'


def delete_contact():
    name = input('Введите имя или фамилию контакта, которого хотите удалить:  ')

    with open(phone_number, 'r', encoding='UTF-8') as file:
        data = json.load(file)
        for i in range(0, len(data)):
            if name == data[i]['имя'] or name == data[i]['фамилия']:
                del data[i]
      
    with open(phone_number, 'w', encoding='UTF-8') as file:
        json.dump(data, file, indent=4)
    print('\nКонтакт удалён!\n')
    controller.user_choice()