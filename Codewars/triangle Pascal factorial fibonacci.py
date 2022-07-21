n = 3
triangle = []
for i in range(n):
    row = [1] * (i + 1)
    for j in range(i + 1):
        if j != 0 and j != i:
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
    triangle.append(row)
print(triangle)
for el in triangle:
    print(el)

# my_list = []
# for el in range(n):
#     row = [1] * (el + 1)
#     for el2 in range(1, el):
#         row[el2] = my_list[el - 1][el2 - 1] + my_list[el - 1][el2]
#     my_list.append(row)
# for el in my_list:
#     print(el)

# n = int(input('input int num: '))
# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     elif n > 0:
#         return n * factorial(n - 1)
#     else:
#         return 'Factorial должен быть положительным числом или 0'
# print(f'Factorial num {n} = ', factorial(n))
#
# def fib(n):
#     if n == 0 or n == 1:
#         return 0
#     elif n == 2:
#         return 1
#     else:
#         return fib(n - 1) + fib(n - 2)
# print(f'Fibonacci num {n} = ', fib(n))





