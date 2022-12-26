#Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

onearray = list(map(int, input("Введите элементы списка через пробел: ").split()))
newarray = []
 
for i in onearray: 
 if i not in newarray:
  newarray.append(i)   
print(f"Список неповторяющихся элементов: {newarray}")