'''Задача 2
Найдите сумму цифр трехзначного числа.
Пример:
123 -> 6 (1 + 2 + 3)
100 -> 1 (1 + 0 + 0)'''

num = input('Введите 3-х значное число: ')
result = 0
if len(num) == 3:
    for i in num:
        result += int(i)
    print(result)
else:
    print('Вы ввели не 3-х значное число')