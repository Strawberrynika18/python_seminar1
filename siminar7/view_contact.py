import json
import controller

phone_number = 'phone_number.json'

def view_contacts():

    with open(phone_number, 'r', encoding='UTF-8') as file:
        data = json.load(file)
        for i in range(0, len(data)):
            print(data[i])
    controller.user_choice()