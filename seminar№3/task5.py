#Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

n = int(input('Введите целое число'))

if n < 0: n = n*-1
f1 = 1
f2 = 1
array = [f1, f2]

for i in range(2, n): 
    f1,f2 = f2, f1 + f2
    array.append(f2)
f1=1
f2=1

for i in range(-n, 1): 
    f1,f2 = f2, f1 - f2
    array.insert(0, f2)
print(array)
