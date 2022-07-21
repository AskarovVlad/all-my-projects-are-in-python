# 1) Дан список словарей persons в формате [{"name": "John", "age": 15}, ... ,{"name": "Jack", "age": 45}]
# а) Напечатать имя самого молодого человека. Если возраст совпадает - напечатать все имена.
# б) Напечатать самое длинное имя. Если длина имени совпадает - напечатать все имена.
# в) Посчитать среднее количество лет всех людей из списка.
persons = [{"name": "Johnni", "age": 15},
           {"name": "Alisa", "age": 15},
           {"name": "Jackie", "age": 45}]
age_list = [el['age'] for el in persons]
print("в)", sum(age_list) // len(persons))
for el in persons:
    if el['age'] == min(age_list):
        print('a)', el['name'])
name_list = [len(el['name']) for el in persons]
for el in persons:
    if len(el['name']) == max(name_list):
        print("б)", el['name'])
print("############################################")
# 2) Даны два словаря my_dict_1 и my_dict_2.
# а) Создать список из ключей, которые есть в обоих словарях.
# б) Создать список из ключей, которые есть в первом, но нет во втором словаре.
# в) Создать новый словарь из пар {ключ:значение}, для ключей, которые есть в первом, но нет во втором словаре.
my_dict_1 = {'name': 'Frosya', 'age': 18, 'city': 'Odessa', 'hobbies': 'music'}
my_dict_2 = {'name': 'Gosha', 'age': 6, 'male': 'dog', 'hobbies': 'eating'}
keys_list_union = [keys for keys in my_dict_1.keys() if keys in my_dict_2.keys()]
# for keys1 in my_dict_1.keys():
#     if keys1 in my_dict_2.keys():
#         keys_list_union.append(keys1)
print(keys_list_union)
print("б) ##################")
keys_list_dif = [keys for keys in my_dict_1.keys() if keys not in my_dict_2.keys()]
# for keys1 in my_dict_1.keys():
#     if keys1 not in my_dict_2.keys():
#         keys_list_dif.append(keys1)
print(keys_list_dif)
print("в) ##################")
my_dict_3 = {keys: value for keys, value in my_dict_1.items() if keys not in my_dict_2.keys()}
# for keys1, values in my_dict_1.items():
#     if keys1 not in my_dict_2.keys():
#         my_dict_3[keys1] = values
print(my_dict_3)
print("г) ##################")
# г) Объединить эти два словаря в новый словарь по правилу:
# если ключ есть только в одном из двух словарей - поместить пару ключ:значение,
# если ключ есть в двух словарях - поместить пару {ключ: [значение_из_первого_словаря, значение_из_второго_словаря]}
my_dict_1 = {'name': 'Frosya', 'age': 18, 'city': 'Odessa', 'hobbies': 'music'}
my_dict_2 = {'name': 'Gosha', 'age': 6, 'male': 'dog', 'hobbies': 'eating'}
my_dict_4 = {k1: [v1, v2] for k1, v1 in my_dict_1.items() for k2, v2 in my_dict_2.items() if k1 == k2}
my_dict_4.update((k1, v1) for k1, v1 in my_dict_1.items() if k1 not in my_dict_4)
my_dict_4.update((k2, v2) for k2, v2 in my_dict_2.items() if k2 not in my_dict_4)
print(my_dict_4)
my_list1 = list('qwerty')
my_list2 = list('123456')
my_dict_6 = dict(zip(my_list1, my_list2))
print(my_dict_6)
print(my_dict_6.get('q', 'Нет такого ключа'))
print(my_dict_6.get('name', 'Нет такого ключа, бла бла бла'))
my_dict_7 = {**my_dict_1, **my_dict_2}      # если ключ 1 и 2 одинаковы, значение перезаписывается
print(my_dict_7)
my_dict_8 = {**my_dict_2, **my_dict_1}
print(my_dict_8)
price_list = [{"bread": 10}, {"water": 100}, {"banana": 2000}, {"water": 12}]
low_price = []
for price in price_list:
    low_price.append(list(price.values())[0])
print(low_price)
print(min(low_price))
for price in price_list:
    if list(price.values())[0] == min(low_price):
        print(price)
# Посчитать все элементы списка, сколько каждый
lst = [0, 1, 2, 2, 3, 3, 3, 3, 4]
print(len(lst))
print(lst.count(0), lst.count(2))
my_dict = {el: lst.count(el) for el in lst}
print(my_dict)
