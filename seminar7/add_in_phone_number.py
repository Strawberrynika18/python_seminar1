import json
import controller


def create_json():
    json_data = []
    with open('phone_book.json', 'w') as file:
        file.write(json.dumps(json_data, indent=2, ensure_ascii=False))
    controller.user_choice()


def add_to_json():
    name = input("Введите имя: ")
    surname = input('Введите Фамилию: ')
    phone = input('Введите номер телефона: ')
    comment = input('Введите коментарий: ')
    json_data = {
        "Имя": name,
        "Фамилия": surname,
        "Номер телефона": phone,
        "Комментарий": comment,
    }
    data = json.load(open("phone_book.json"))
    data.append(json_data)
    with open("phone_book.json", "w") as file:
        json.dump(data, file, indent=2, ensure_ascii=False)
    print('\nДобавлен новый контакт!\n')
    controller.user_choice()