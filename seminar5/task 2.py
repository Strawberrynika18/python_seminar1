#Создайте программу для игры с конфетами человек против человека. Реализовать игру игрока против 
# игрока в терминале. Игроки ходят друг за другом, вписывая желаемое количество конфет. 
# Первый ход определяется жеребьёвкой. В конце вывести игрока, который победил


# На столе лежит 221 конфета. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход.


from random import randint


def input_dat(name): #ввод кол-ва конфет
    x = int(input(f"{name}, введите количество конфет, которое возьмете от 1 до 28: "))
    while x < 1 or x > 28:
        x = int(input(f"{name}, введите корректное количество конфет: "))
    return x


def p_print(name, k, counter, value):
    print(f"Ходил {name}, он взял {k}, теперь у него {counter}. Осталось на столе {value} конфет.")


player1 = input("Введите имя 1-го игрока: ")
player2 = input("Введите имя 2-го игрока: ")
value = 221
flag = randint(0, 2)  #очередность
if flag:
    print(f"Первый ходит {player1}")
else:
    print(f"Первый ходит {player2}")

counter1 = 0
counter2 = 0

while value > 28:
    if flag:
        k = input_dat(player1)
        counter1 += k
        value -= k
        flag = False
        p_print(player1, k, counter1, value)
    else:
        k = input_dat(player2)
        counter2 += k
        value -= k
        flag = True
        p_print(player2, k, counter2, value)

if flag:
    print(f"{player1} победил ")
else:
    print(f"{player2} победил ")