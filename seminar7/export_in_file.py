import json
import controller


phone_number = 'phone_number.json'

def export_txt():
 

    with open(phone_number, 'r', encoding='UTF-8') as file:
        data = json.load(file)
        for i in range(0, len(data)):
                with open('Export_phone_book.txt', 'a') as export:
                    export.write('\n' + "".join(data[i]['Имя']) + ' ' + "".join( data[i]['Фамилия']) + ' ' + "".join(data[i]['Номер телефона']) + ' ' + "".join(data[i]['Комментарий']))

    print('\nКонтакты успешно экспортированы в файл!\n')
    contriller.user_choice()