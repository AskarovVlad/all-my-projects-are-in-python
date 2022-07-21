# bool(0)     # True, False(только для 0 и None
# s = 'Hello'
# dir(s)
# eval('print(3-1)')    # запускает программу в скобках
# exec('''a=10
# b=20
# c=a+b
# print(c)''')    # запускает сложнее программу в скобках
# print(int(2.5))
# print(int(float("5.5")))
# x = (10, 20, 30, 40, 50)
# print(sum(x))
# # print(sum(x[0:4]))
# f = open('File.txt', 'w')
# f.write('Hello my file')
# f.close()
# f = open('File.txt')
# x = f.read()
# print(list(x))
# y = list(x)
# print("".join(y))
# j = 100
# for i in range(0, 5):
#     # print(i)
#     # print(i, end=" ")
#     print(i, j, sep="+", end=" ")
# end-окончание каждого значения, по умолч \n перенос на след, sep- разделитель, при выводе разных переменных
def func(x, y):
    print(f' a= {x}, b={y}')
func(10, 20)
print('Введите а')
try:    # попытка
    a = input()
    procent = float(100/int(a))
    print(round(procent, 2))
except ValueError:  # кроме
    print("Ввели симфолы, попробуйте еще раз.")
except ZeroDivisionError:
    print("Ввели ноль, попробуйте еще раз")
else:   # выполняется если не было ошибок
    print("Не было ошибок")
finally:
    print("Выполняется всегда")
