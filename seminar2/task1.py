#Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# x = input('Введите число ')
# y=x.split (".")
# print (y)
# for i in range (len(y)):
#   y[i]=int (y[i])
#   print (y)

def sum_item_of_number(num):
    return sum(map(int, num.replace('.','').replace('-','')))

num = input('Введите любое вещественное число: ')
print(f'Сумма цифр  равна {sum_item_of_number(num)}')