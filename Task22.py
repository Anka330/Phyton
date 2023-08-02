# Задача 22: 
# Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, 
# которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. 
# n — кол-во элементов первого множества. 
# m — кол-во элементов второго множества. 
# Затем пользователь вводит сами элементы множеств.  


print("Введите число N:")
n = int(input())
print("Введите число M:")
m = int(input())
list1 = list()
list2 = list()

for i in range(n):
    print(f'Введите {i+1}-е число множества N:')
    k = int(input())
    list1.append(k)

for i in range(m):
    print(f'Введите {i+1}-е число множества M:')
    k = int(input())
    list2.append(k)
print(list1)
print(list2)

set1 = set(list1)
print(set1)

set2 = set(list2)
print(set2)

intersect = set1.intersection(set2)

list3 = list(intersect)
list3.sort()
print (f'числа, которые встречаются в обоих наборах{list3}')