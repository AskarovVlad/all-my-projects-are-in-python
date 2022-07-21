# 1. Дан список строк my_list. Создать новый список в который поместить
# элементы из my_list по следующему правилу:
# Если строка стоит на нечетном месте в my_list, то ее заменить на
# перевернутую строку. "qwe" на "ewq".
# Если на четном - оставить без изменения.
# Задание сделать с использованием enumerate или range.
my_list = ['qwe', 'asd', 'zxc', 'abc', 'defg']
new_list = []
for index, value in enumerate(my_list):
    if index % 2:
        new_list.append(value)
    else:
        new_list.append(value[::-1])
print(new_list)
new_list1 = [value[::-1] if index % 2 == 0 else value for index, value in enumerate(my_list)]
print(new_list1)
print('2) #####################################')
# 2. Дан список строк my_list. Создать новый список в который поместить
# элементы из my_list у которых первый символ - буква "a".
my_list2 = ['zewa', 'asd', 'zxc', 'abc', 'defg', 'rpg']
new_list2 = []
for element in my_list2:
    if element.startswith('a'):
        new_list2.append(element)
print(new_list2)
new_list3 = [element for element in my_list2 if element.startswith('a')]
print(new_list3)
print('3) #####################################')
# 3. Дан список строк my_list. Создать новый список в который поместить
# элементы из my_list в которых есть символ - буква "a" на любом месте.
my_list3 = ['123', '456a', 'zewa', 'asd', '7890', 'zxc', 'abc', 'defag', 'rapg']
new_list3 = []
for element in my_list3:
    if 'a' in element:
        new_list3.append(element)
print(new_list3)
new_list4 = [element for element in my_list3 if 'a' in element]
print(new_list4)
print('4) #####################################')
# 4. Дан список my_list в котором могут быть как строки (type str) так и целые числа (type int).
# Создать новый список в который поместить только строки из my_list.
my_list4 = ['123', 'a456a', 'zewa', 'asd', '7890', 'zxc', 'abc', 'defag', 'rapg']
new_list4 = [element for element in my_list4 if element.isalpha()]
# for element in my_list4:
#     if element.isalpha():
#         new_list4.append(element)
print(new_list4)
print('5) #####################################')
# 5. Дана строка my_str. Создать список в который поместить те символы из my_str,
# которые встречаются в строке только один раз.
my_str5 = 'sdjng;soinqerwrww'
my_list5 = list(set(my_str5))
print(my_list5)
print('6) #####################################')
# 6. Даны две строки. Создать список в который поместить те символы,
# которые есть в обеих строках хотя бы раз.
str1 = 'Hello, my name is Eugene and i want to sleep, what about you?'
str2 = 'Do you want to make some coffee?'
new_list6 = [element for element in set(str1).intersection(set(str2))]
print(new_list6)
print('7) #####################################')
# 7. Даны две строки. Создать список в который поместить те символы, которые есть в обеих строках,
# но в каждой только по одному разу.
str1 = 'qwerty-123-ytrewq_zxcv'
str2 = '456_zxcv_qwerty-qwerty-321'
str1_2_set = set(str1).intersection(set(str2))
new_list7 = []
for symbol in str1_2_set:
    if symbol in str1:
        count1 = str1.count(symbol)
    if symbol in str2:
        count2 = str2.count(symbol)
        if count1 == 1 and count2 == 1:
            new_list7.append(symbol)
print(new_list7)

print('8) #####################################')
# 8. Описать с помощью словаря следующую структуру для конкретного человека (можно придумать):
# Фамилия
# Имя
# Возраст
# Проживание
#     Страна
#     Город
#     Улица
# Работа
#     Наличие
#     Должность

# 9. Описать с помощью словаря следующую структуру (рецепт ненастоящего торта,
# придумать и указать граммы для продуктов):
# Составляющие
#     Коржи
#         Мука
#         Молоко
#         Масло
#         Яйцо
#     Крем
#         Сахар
#         Масло
#         Ваниль
#         Сметана
#     Глазурь
#         Какао
#         Сахар
#         Масло
print('Lesson Test ###################################################')
my_gen_list = [number ** 2 for number in range(15)]
print(my_gen_list)
alphabet_list = [chr(index) for index in range(ord('A'), ord('Z') + 1)]
print(alphabet_list)
alphabet_list.insert(3, 'F')
print(alphabet_list)
print(alphabet_list.index('F', 4, 7))
my_set = set(my_gen_list).union(set(alphabet_list))
print(my_set)
my_list6 = ['aaa', 'bbb', 'bbb', 'ccc', 'ccc', 'ccc']
for value in set(my_list6):
    count = my_list6.count(value)
    print(value, count)
