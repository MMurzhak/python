'''Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером. 
Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. 
Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.
*Пример:*
385916 -> yes
123456 -> no '''

import os
os.system('cls')

ticket = input('Введите 6-значный номер билета: ')
if len(ticket) != 6:
    print(f'Число {ticket} не 6-ти значное')
else:
    res1 = 0
    res2 = 0
    for i in range(len(ticket)//2):
        res1 += int(ticket[i])
        print(res1)
        res2 += int(ticket[len(ticket)//2 + i])
        print(res2)
    if res1 == res2:
        print(f'{ticket} счастливый номер')
    else:
        print(f'{ticket} не счастливый номер')