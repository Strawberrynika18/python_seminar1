#задача 2
#Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
for x in range(2):
        for y in range(2):
            for z in range(2):
               print(not (x or y or z) == (not x and not y and not z))
            if not (x or y or z) == (not x and not y and not z): # проверка условия и ,если условие истино, выводятся значения x,y и z 
                    print(x,y,z)

