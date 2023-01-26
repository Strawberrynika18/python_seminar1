from write_information import count_inf

def input_information():
    dct = dict()
    Id = count_inf("name.txt") 
    dct["id"] = Id     
    dct["surname"] = input('Введите Фамилию: ')
    dct["name"] = input('Введите Имя: ')
    dct["class"] = input('Введите Класс: ')
    dct["status"] = input('Введите Статус: ')
    dct["row"] = input('Введите Ряд: ')
    dct["col"] = input('Введите Номер парты: ')
    dct["city"] = input('Введите Город: ')
    dct["street"] = input('Введите Улица: ')
    dct["house"] = input('Введите Дом: ')
    dct["apartament"] = input('Введите Квартира: ')
    dct["other"] = input('Введите Примечание: ')
    return dct