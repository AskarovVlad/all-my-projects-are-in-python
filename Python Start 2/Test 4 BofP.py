# from math import *
#
# n = int(input("Введите диапазон:- "))
# p = [2, 3]
# count = 2
# a = 5
# while count < n:
#     b = 0
#     for i in range(2, a):
#         if i <= sqrt(a):
#             if a % i == 0:
#                 print(a, "непростое")
#                 b = 1
#             else:
#                 pass
#     if b != 1:
#         print(a, "простое")
#         p = p + [a]
#     count = count + 1
#     a = a + 2
# print(p)
# print(sqrt(100))

# sp = []
# for i in range(20):
#     if i % i == 0

# zoo = 'python', 'elefhant', 'lion'
# print(type(zoo))
# a = {'1', '2', '3', '4', '5', 'lion', 'wolf'}
# print(a)
# print(type(a))
# b = a.copy()
# print(b)
# b.remove('3')
# b.remove('lion')
# print(b)
# print('________')
# print(a & b)
# print(a.intersection(b))    # печатает общие элементы
# name = 'Swaroop is very hungry'    # Это объект строки
# if name.startswith('Swa'):
#     print('Да, строка начинается на "Swa"')
# if 'a' in name:
#     print('Да, она содержит строку "a"')
# if name.find('war'):
#     print('Да, она содержит строку "war"')
# print(name.split(" "))
# name1 = name.replace(" ", '')   # заменять
# print(name1)
# name2 = name[-1::-1]
# print(name2)
# list1 = ['1', '2', '3', 'look', 'at', 'me']
# print(list1)
# print(id(list1))
# list2 = list1[-1::-1]
# print(list2)
# print(id(list2))
# del list1[0]
# print(list1)
# del list2[2]
# print(list2)
# tuple1 = ('one', 'two', 'three', 'look', 'at', 'me')
# print(tuple1)
# tuple2 = tuple1[-1::-1]
# print(tuple2)
str1 = 'Welcome to home'

# def spin_words(sentence):
#     return sentence[-1::-1]
# print(spin_words(str1))

# def is_square(n):
#     if n < 0:
#         print(f'{n} -> False')
#     if sqrt(n) == int(sqrt(n)):
#         print(f'{n} -> True')
#     else:
#         print(f"{n} -> False")
# import math
#
#
# def is_square(n):
#     return n > -1 and math.sqrt(n) % 1 == 0


# print(is_square(4))
n = 10.1 % 1
print(n)
import math

print(math.floor(-32.1))
a = 10
print(bool(11 < a > 20))
s = 'Hello World lalaland'
print(s.count('o', 5, 8))
print(s.replace("l", '+', 4))
print(s.isalpha())  # только из букв, без символом
i = '19898'
print(i.isdigit())  # только из цифр
print(i.rjust(10, '-'))
