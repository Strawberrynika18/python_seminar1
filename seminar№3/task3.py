#Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
n = [1.1, 1.2, 3.1, 5, 10.01]
array = []
for i in range(len(n)):
    if n[i] % 1 != 0:
        array.append(n[i])
n2 = [round(array[i] % 1, 2) for i in range(len(array))]
rasn=max(n2)-min(n2)
print(f"{n2} => {rasn}")
