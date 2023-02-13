# Задача 26:  Напишите программу, которая на вход принимает два числа A и B,
#  и возводит число А в целую степень B с помощью рекурсии.
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8

# a = int(input("Введите число А: ")) 
# b = int(input("Введите число B: "))
# n = 1
# k = 1
# def exponent(a, b, n, k):
#     if b == 0:
#         return print(1)
#     else:
#         n = n * a     
#     if k < b:
#         k += 1            
#         exponent(a, b, n, k)
#     else:
#        return print(n)   
# exponent(a, b, n, k)         





# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
#  Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
# 2 2
# 4


# a = int(input("Введите число а = " ))
# b = int(input("Введите число b = " ))
# s = 0
# k = 0
# l = 0
# def sum_ab(a, b, s, k, l):
#     if a == 0:
#         print("сумма a и b =", b)
#         return b   
#     if b == 0:
#         print("сумма a и b =", a)
#         return a 
#     else:        
#         if k < a:
#             k += 1              
#             sum_ab(a, b, s, k, l)
#         else:
#             if l < b:
#                 l += 1
#                 s = k + l       
#                 sum_ab(a, b, s, k, l)
#             else:
#                 print("сумма a и b =", s)
#                 return s       
# sum_ab(a, b, s, k, l)