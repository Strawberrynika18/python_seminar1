#задача 5
#Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
ax = float(input('Введите значение x первой точки:')) #вещественный тип
ay = float(input('Введите значение y первой точки:'))
bx = float(input('значение x второй точки:'))
by = float(input('Введите значение y второй точки:'))

import math
interval = math.sqrt((ax-bx)**2+(ay-by)**2)
print(f'Растояние между точкой A до точки B = {interval}' )