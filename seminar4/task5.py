#Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.


import random


def write_file(name, st): #записываю в файл
    with open(name, 'w') as file:
        file.write(st)

def rand():
    return random.randint(0, 101)

def mn(k): 
    array = [rand() for i in range(k+1)]
    return array 


def create_st(sp):
    array  = sp[::-1]
    wr = ''
    if len(array) < 1:
        wr = 'x = 0'
    else:
        for i in range(len(array )):
            if i != len(array ) - 1 and array [i] != 0 and i != len(array ) - 2:
                wr += f'{array [i]}x^{len(array )-i-1}'
                if array [i+1] != 0 or array [i+2] != 0:
                    wr += ' + '
            elif i == len(array ) - 2 and array [i] != 0:
                wr += f'{array [i]}x'
                if array [i+1] != 0 or array [i+2] != 0:
                    wr += ' + '
            elif i == len(array ) - 1 and array [i] != 0:
                wr += f'{array [i]} = 0'
            elif i == len(array ) - 1 and array [i] == 0:
                wr += ' = 0'
    return wr


def sq_mn(k): #получаю степень
    if 'x^' in k:
        i = k.find('^')
        num = int(k[i+1:])
    elif ('x' in k) and ('^' not in k):
        num = 1
    else:
        num = -1
    return num


def k_mn(k):
    if 'x' in k:
        i = k.find('x')
        num = int(k[:i])
    return num


def calc_mn(st):
    st = st[0].replace(' ', '').split('=')
    st = st[0].split('+')
    array  = []
    l = len(st)
    k = 0
    if sq_mn(st[-1]) == -1:
        array.append(int(st[-1]))
        l -= 1
        k = 1
    i = 1  
    ii = l-1  
    while ii >= 0:
        if sq_mn(st[ii]) != -1 and sq_mn(st[ii]) == i:
            array .append(k_mn(st[ii]))
            ii -= 1
            i += 1
        else:
            array .append(0)
            i += 1

    return array 


#создание файлов
k1 = int(input("Введите  степень для 1 файла k = ")) 
koef1 = mn(k1)
write_file("file5_1.txt", create_st(koef1))
k2 = int(input("Введите степень для 2 файла k = "))
koef2 = mn(k2)
write_file("file5_2.txt", create_st(koef2))

#нахождение суммы
with open('file5_1.txt', 'r') as file: 
    st1 = file.readlines()
with open('file5_2.txt', 'r') as file:
    st2 = file.readlines()
print(f"содержимое 1 файла: {st1}")
print(f"содержимое 2 файла: {st2}")
array1 = calc_mn(st1)
array2 = calc_mn(st2)
ll = len(array1)
if len(array1) > len(array2):
    ll = len(array2)
newarray = [array1[i] + array2[i] for i in range(ll)]
if len(array1) > len(array2):
    mm = len(array1)
    for i in range(ll, mm):
        newarray.append(array1[i])
else:
    mm = len(array1)
    for i in range(ll, mm):
        newarray.append(array2[i])
write_file("file5_res.txt", create_st(newarray))
with open('file5_res.txt', 'r') as file:
    st3 = file.readlines()
print(f"результат =  {st3}")


