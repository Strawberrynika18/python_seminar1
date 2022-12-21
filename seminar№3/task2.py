# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

n = [2, 3, 4, 5, 6]

def newlist(list):
    if len(list) % 2 != 0:
        items = len(list)//2 + 1
    else:
        len(list)//2
    new = [list[i]*list[len(list)-i-1] for i in range(items)]
    print(new)

newlist(n)


