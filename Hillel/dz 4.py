# Задания:
# 1) У вас есть список my_list с значениями типа int.
# Распечатать те значения, которые больше 100.
# Задание выполнить с помощью цикла for.
my_list = [10, 200, 330, 4, 555, 343]
for el in my_list:
    if el > 100:
        print(el, end=' ')
print('######')
# 2) У вас есть список my_list с значениями типа int, и пустой список my_results.
# Добавить в my_results те значения, которые больше 100.
# Распечатать список my_results.
# Задание выполнить с помощью цикла for.
my_list1 = [1, 228, 3300, 44, 555, 613]
my_results1 = []
for el in my_list1:
    if el > 100:
        my_results1.append(el)
print(my_results1)
# 3) У вас есть список my_list с значениями типа int.
# Если в my_list количество элементов меньше 2, то в конец добавить значение 0.
# Если количество элементов больше или равно 2, то добавить сумму последних двух элементов.
# Количество элементов в списке можно получить с помощью функции len(my_list)
my_list2 = [1, 2, 3, 40, 50, 600, 7, 8]
if len(my_list2) <= 2:
    my_list2.append(0)
else:
    my_list2.append(my_list2[-1] + my_list2[-2])
print(my_list2)
# #####################################################
# Еще один пример - вложенные циклы (цикл в цикле).
# my_string_1 = "12"
# my_string_2 = "34"
# for symb_1 in my_string_1:
# 	for symb_2 in my_string_2:
# 		print(symb_1 + symb_2)
#
#
#
# Результат:
# "13"	# перебирается все элементы из my_string_2 для элемента "1" из my_string_1
# "14"
# "23"	# перебирается все элементы из my_string_2 для элемента "2" из my_string_1
# "24"
# #####################################################
#
# 4) У вас есть строка my_string = '0123456789'.
# Сгенерировать целые числа (тип int) от 0 до 99 и поместить их в список.
# Задание нужно выполнить ТОЛЬКО через цикл в цикле(См. пример выше) и приведение типов.
# Генерирование через range или другие "фишки" я засчитывать не буду ))
my_string = '0123456789'
new_lst = []
for symbol_1 in my_string:
    for symbol_2 in my_string:
        new_lst.append(int(symbol_1 + symbol_2))
print(new_lst, type(new_lst[1]))