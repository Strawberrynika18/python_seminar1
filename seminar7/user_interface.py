import right_phone_number
from export_in_file import phone_number


def start():
    greetings = 'Здравствуй!\nЗдесь вы можете создать новый контакт, найти его, изменить или удалить,\nпоказать все контакты.'

    print(f'{greetings}\n')


def menu():
    what_to_do = 'Выберите цифру в меню для совершения действия:'
    new_book = '0. Создать новую книгу или очистить уже имеющуюся'
    add_in_phone_book = '1. Добавить новый контакт'
    change_number = '2. Изменить номер телефона'
    change_sirname = '3. Изменить фамилию'
    delete_phone_number = '4. Удалить контакт'
    view_contact = '5. Показать все контакты'
    export_in_file = '6. Экспортировать контакты в файл'
    to_exit = '7. Выход'
    print(f'{what_to_do}\n\n{new_book}\n{ add_in_phone_book }\n{change_number}\n{change_sirname}\n{delete_phone_number}\n{view_contact}\n{export_in_file}\n{to_exit}')
    return change_phone_number.digit_check()