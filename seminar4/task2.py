#Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

n = int(input("Введите натуральное число: "))
n2=n #создаю доп.переменную для вывода введенного числа, так как оно меняется 
i=2 #первое простое число
onearray = []
 
while i <= n:
    if n % i == 0:
        onearray.append(i)
        n //= i
        i = 2
    else:
        i += 1
print(f"Простые множители числа {n2}: {onearray}")