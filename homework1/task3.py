#задача 3
# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

x = int(input('Введите число x, отличное от 0:'))
y = int(input('Введите число y, отличное от 0:'))

if x > 0 and y > 0:
    print(' точка находится в плоскости 1 ')
elif x < 0 and y > 0:
    print('точка находится в плоскости 2 ')
elif x < 0 and y < 0:
    print(' точка находится в плоскости 3 ')
elif x > 0 and y < 0:
    print(' точка находится в плоскости 4 ')
elif x==0 and y == 0:
    print('смотрите внимательно условие ввода данных')