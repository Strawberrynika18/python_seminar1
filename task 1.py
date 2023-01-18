#Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
#С помощью использования лямбд, filter, map, zip, enumerate, list comprehension

from functools import reduce

a = list(map(int, input('Введите  координаты первой точки  через пробел: ').split())) 
b = list(map(int, input('Введите координаты второй точки  через пробел: ').split()))

def distance (a, b):
     res= reduce(lambda x, y: (x + y)**(1/2), (map(lambda dot: (dot[1] - dot[0])**2, zip(a, b))))
     return round(res, 2)

print(distance(a, b))