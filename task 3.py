#Найти произведение пар чисел списка(парой считаем первый и последний, второй предпоследний и тд)

import math

list_a = list(map(int, input('Введите элементы списка через пробел: ').split()))
print("Список: ",list_a)
res = list([a*b for a,b in zip(list_a[0:math.ceil(len(list_a)/2)],list_a[::-1])])
print('Список произведения пар: ', res)