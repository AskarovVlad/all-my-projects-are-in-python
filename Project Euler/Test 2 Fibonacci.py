# Весь ряд фибоначчи
# n = int(input())
# lst = [1, 1]
# numb_n = 0
# while len(lst) < n:
#     numb_n = lst[-2] + lst[-1]
#     lst.append(lst[-2] + lst[-1])
# print(numb_n)
# # print(*lst)
# fib1 = 1
# fib2 = 1
# # n = int(input("Номер елемента ряда Фиббоначи:\n"))
# n = 7
# i = 0
# fib = [fib1, fib2]
# while i < n - 2:
#     fib_sum = fib1 + fib2
#     fib1 = fib2
#     fib2 = fib_sum
#     i += 1
#     for i in range(0, fib_sum < 4000000):
#         fib.append(fib_sum)
# print('Значение этого элемента:', fib_sum)
#
# print(*fib)
# sum_i = 0
# for i in fib:
#     if i % 2 == 0:
#        sum_i += i
# print(sum_i)
#
# def fib(n):
#     if n in (1, 2):
#         return 1
#     return fib(n - 1) + fib(n - 2)
#
#
# print(fib(10))
# x = 600851475143

cache = {0: 0, 1: 1}


def fast_fib(n):
    if n not in cache:
        cache[n] = fast_fib(n - 1) + fast_fib(n - 2)
    return cache[n]


print(fast_fib(900))
