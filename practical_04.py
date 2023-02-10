# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с
# повторениями). Выдать без повторений в порядке возрастания все те числа, которые
# встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
# элементов второго множества. Затем пользователь вводит сами элементы множеств.

# Пример
# 11 6
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18
# 6 12
#                Решение
# import random
# n = int(input("Кол-во элементов первого множества: ")) 
# m = int(input("Кол-во элементов второго множества: "))
# N = [random.randint(0,10) for _ in range(n)]
# # N = [int(input()) for i in range(N)] # Вводим элементы массива c клавиатуры 
# M = [random.randint(0,10) for _ in range(m)]
# # M = [int(input()) for i in range(M)] # Вводим элементы массива c клавиатуры
# a = {i for i in N}
# b = {i for i in M}
# # print("Элементы первого списка:", N)
# print("Элементы первого множества:", *a)
# # print("Элементы второго списка:", M)
# print("Элементы второго множества:", *b)
# c = a.intersection(b)
# print("Общие элементы множеств:   ",*c)



# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растет на
# круглой грядке, причем кусты высажены только по окружности. Таким образом, у
# каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них
# выросло различное число ягод – на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники.
# Эта система состоит из управляющего модуля и нескольких собирающих модулей.
# Собирающий модуль за один заход, находясь непосредственно перед некоторым
# кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может
# собрать за один заход собирающий модуль, находясь перед некоторым кустом
# заданной во входном файле грядки.

# Пример
# 4 -> 1 2 3 4
# 9

# Решение

# import random
# n = int(input("Кол-во кустов 'N': "))
# a = int(input("Введите максимальное кол-во ягод на кусте 'a': "))
# N = [random.randint(1,a) for _ in range(n)]
# print("Кол-во ягод на каждом кусте:", *N)
# m = 3
# max = t = N[1-m] + N[2-m] + N[0]
# for i in range(n-1):
#     if i < n - 1:          
#             t = t - N[i-(m-1)] + N[i + (m-2)]
#             i += 1
#             if t > max:
#                 max = t
# print("Максимальное кол-во ягод с трех кустов:", max)

