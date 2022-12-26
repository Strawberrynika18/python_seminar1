#Задана натуральная степень k. 
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

import random

k = int(input("Введите  степень k = "))

def creatfile(st): #запись в файл "file4.txt"
    with open('file4.txt', 'w') as file: 
        file.write(st)


def rand(): #формирование случ. образом
    return random.randint(0, 101)


def mn(k):   #с используем рандомные значения
    array = [rand() for i in range(k+1)]
    return array


def create_st(sp): #создаем  и записываем строку в строку
    array = sp[::-1]
    note = ''
    if len(array) < 1:
        wr = 'x = 0'
    else:
        for i in range(len(array)):
            if i != len(array) - 1 and array[i] != 0 and i != len(array) - 2:
                note += f'{array[i]}x^{len(array)-i-1}'
                if array[i+1] != 0:
                   note += ' + '
            elif i == len(array) - 2 and array[i] != 0:
                note += f'{array[i]}x'
                if array[i+1] != 0:
                    note += ' + '
            elif i == len(array) - 1 and array[i] != 0:
                note += f'{array[i]} = 0'
            elif i == len(array) - 1 and array[i] == 0:
                note += ' = 0'
    return note

k2 = mn(k)
creatfile(create_st(k2))