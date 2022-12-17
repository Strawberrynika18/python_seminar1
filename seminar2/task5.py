#Реализуйте алгоритм перемешивания списка.
import random #подключ. для рандомного перемешивания элементов
def mix(items):
    list = items[:]
    length = len(list)
    for i in range(length):
        index = random.randint(0, length - 1)
        temp = list[i]
        list[i] = list[index]
        list[index] = temp
    return list
list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
mix = mix(list)
print("список: ")
print(list)
print("перемешанный список: ")
print(mix)