# 1 Дано целое число (int). Определить сколько нулей в этом числе.
x = 416100001201000
print(str(x).count('0'))
# 2 Дано целое число (int). Определить сколько нулей в конце этого числа. Например для числа 1002000 - три нуля
my_int = 1002000
# count = len(str(my_int)) - len(str(int(str(my_int)[::-1]))) много лишнего
count = len(str(my_int)) - len(str(my_int).rstrip("0"))
print(count)
print(str(my_int).rstrip('0'))
print('###############################')
# 3 Даны списки my_list_1 и my_list_2.
# Создать список my_result в который вначале поместить
# элементы на четных местах из my_list_1, а потом все элементы на нечетных местах из my_list_2.
my_list_1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
my_list_2 = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
my_result = my_list_1[1::2] + my_list_2[::2]
print(my_result, id(my_result))
result = []
print(id(result))
result.extend(my_list_1[1::2])
result.extend(my_list_2[::2])
print(result, id(result))
print('4 ###############################')
# 4 Дан список my_list. СОЗДАТЬ НОВЫЙ список new_list у которого первый элемент из my_list
# стоит на последнем месте. Если my_list [1,2,3,4], то new_list [2,3,4,1]
my_list = [1, 2, 3, 4]
new_list = my_list[1:] + my_list[:1]
print(new_list)
print('5 ###############################')
# 5.Дан список my_list. В ЭТОМ списке первый элемент переставить на последнее место.
# [1,2,3,4] -> [2,3,4,1]. Пересоздавать список нельзя! (используйте метод pop)
my_list3 = [1, 2, 3, 4, 5]
print(id(my_list3))
# my_list3.append(my_list3[0])
# my_list3.pop(0)
my_list3.append(my_list3.pop(0))
print(my_list3, id(my_list3))
print('6 ###############################')
# 6 Дана строка в которой есть числа (разделяются пробелами).
# Например "43 больше чем 34 но меньше чем 56". Найти сумму ВСЕХ ЧИСЕЛ (А НЕ ЦИФР) в этой строке.
# Для данного примера ответ - 133. (используйте split и проверку isdigit)
my_str = "43 больше чем 34     , но меньше чем 56"
my_list4 = my_str.split()
print(my_list4)
my_list5 = []
for nums in my_list4:
    if nums.isdigit():
        my_list5.append(int(nums))
print(sum(my_list5))
print('7 ###############################')
# 7 Дана строка my_str в которой символы МОГУТ повторяться и два символа l_limit, r_limit,
# которые точно находятся в этой строке. Причем l_limit левее чем r_limit.
# В переменную sub_str поместить НАИБОЛЬШУЮ часть строки между этими символами.
# my_str = "My long string", l_limit = "o", r_limit = "g" -> sub_str = "ng strin".
my_str = "My long string"
l_limit = 'o'
r_limit = 'g'
l_index = my_str.find(l_limit)
r_index = my_str.rfind(r_limit)
sub_str = my_str[l_index + 1:r_index]
print(sub_str)
print('8 ###############################')
# 8. Дана строка my_str. Разделите эту строку на пары из двух символов и поместите эти пары в список.
# Если строка содержит нечетное количество символов, пропущенный второй символ последней пары должен
# быть заменен подчеркиванием ('_'). Примеры: 'abcd' -> ['ab', 'cd'], 'abcde' -> ['ab', 'cd', e_']
# (используйте срезы длинны 2)
my_strq = 'abcdefg'
sub_list = []
if len(my_strq) % 2:
    my_strq += "_"
for element in range(len(my_strq) // 2):
    element *= 2
    sub_list.append(my_strq[element: element + 2])
print(sub_list)
print('9 ###############################')
# 9. Дан список чисел. Определите, сколько в этом списке элементов,
# которые больше суммы двух своих соседей (слева и справа), и НАПЕЧАТАЙТЕ КОЛИЧЕСТВО таких элементов.
# Крайние элементы списка никогда не учитываются, поскольку у них недостаточно соседей.
# Для списка [2,4,1,5,3,9,0,7] ответом будет 3 потому что 4 > 2+1, 5 > 1+3, 9>3+0.
lst = [2, 4, 1, 5, 3, 9, 0, 7]
sum_lst = []
count = 0
for index in range(1, len(lst)-2):
    if lst[index] > lst[index - 1] + lst[index + 1]:
        count += 1
        sum_lst.append(lst[index])
print(count, sum_lst)
print('10 ###############################')
# 10. Дана строка my_str, список str_index целых чисел в диапазоне от
# 0 до длинны строки минус 1, пустой список my_list.
# Заполнить my_list символами из my_str, которые стоят на местах с
# индексами из str_index
my_string = "GoodMorning"
str_index = list(range(len(my_string)))
my_list = []
for symbol in str_index:
    my_list.append(my_string[symbol])
print(str_index)
print(my_list)
value = 123456789
new_value = int(str(value)[::-1])
print(new_value, type(new_value))
new_value1 = int("".join(sorted(str(value), reverse=True)))
print(new_value1)
