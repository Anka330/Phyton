# Задача 14: 
# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

# Пример:
# 10 -> 1 2 4 8

n = int(input('Введите число N: '))

step = 0

while 2 ** step <= n:
    print(2 ** step)
    step = step + 1