# name = "Vlad"
# name2 = "Olesia"
# print(f'Привет {name}, {name2}!')
# my_string = "Hello {}, {}!".format(name, name2)
# my_string2 = "Hello {1}, {0}!".format(name, name2)
# my_string3 = "Hello {n}, {n2}!".format(n=name, n2=name2)
# print(my_string)
# print(my_string2)
# print(my_string3)
# print(name2[1:len(name2)])
# my_string4 = "0123456789"
# print(my_string4[:6])
# print(my_string4[1:11:2])   # шаг
# print(my_string4[::-1])
# surname = input("Введите Вашу фамилию: \n")
# print(f"Ваша фамилия: {surname}")
# age = int(input("Введите Ваш возраст: "))
# print(type(age))
# list = ['1', 'lesia', '2', 'vlad']
# list.append('3')    # добавить в конец
# print(list)
# list.insert(0, 'start')
# print(list)
# list.pop()  # удалить
# print(list)
# list.pop(0)
# print(list)
# list2 = ['4', 'mama']
# list.extend(list2)    # расширяет
# print(list)
# list.remove('2')    # удаляет значения, если несколько одинаковых, удаляет первый
# print(list)
# print(list.count('4'))  # показывает сколько раз встречается
# print(list.index('4'))
# list3 = ['0','2', '1', '3', 'а', "я", "р"]
# print(list3)
# list3.sort()    # сортирует по порядку
# print(list3)
# list3.reverse()     # в обратном порядке
# print(list3)
# list4 = " ".join(list3)
# print(list4)
# dict1 = {}
# dict2 = dict()
# print(type(dict1))
# print(type(dict2))
# my_dict1 = {1: 'vlad', 2: "lesia", 3: 'mama', 'four': 'ptn'}
# # print(my_dict1['four'])
# # my_dict1['five'] = 'eat'
# # print(my_dict1)
# # my_dict1[1] = 'oskar'
# # print(my_dict1)
# # del my_dict1[2]
# # print(my_dict1)
# # for k, v in my_dict1.items():
# #     print(f'{k} >>> {v}')
# # for key in my_dict1:
# #     print(key)
# # for key in my_dict1.keys():
# #     print(key)
# if 'five' in my_dict1.keys():
#     print("not")
# else:
#     print("mogno")
# for values in my_dict1.values():
#     print(values)
# person = {'vlad': {'name': "Vlad",
#                    'surname': "Askarov",
#                    'возраст': 26,
#                    'фрукты': ['avokado', 'kivi', 'orange', 'banana']
#                    },
#           "lesia": {'name': "Olesia",
#                     'surname': "Askarova",
#                     'возраст': 25,
#                     'фрукты': ['berry', 'kivi', 'orange', 'ananas']}
#           }
# # for values in person.values():
# #     print(values)
# for username, userinfo in person.items():
#     print(f"Имя пользователя: {username}")
#     age = userinfo['возраст']
#     fruit = userinfo['фрукты']
#
#     print(f'Возраст пользователя {username}: {age} лет.')
#     print(f"Любимые фрукты: {fruit}")
# for k, v in person.items():
#     print(f'{k}')
#     age = v['возраст']
#     fruit = v['фрукты']
#     print(age)
#     print(fruit)
# my_dict = {'vlad': 'Askarov', 'olesia': 'Kuznetsova', 'nick': 'lyah'}
# print(my_dict['olesia'])
# print(my_dict.get('nic', 'wtf dude?'))  # возвращает значение ключа, или любой текст, указанный через запятую
# print(my_dict.setdefault('5', 'magic'))
# print(my_dict)
# print(my_dict.setdefault(67))
# # возвращает знач ключа, но если его нет, добавляет его в словарь, если он пуст, добавляет в ключ знач None
# print(my_dict)
# md2 = my_dict.copy()
# print(md2)
# md2.update({'job': 'programmer'})  # если ключ существует, его значение будет перезаписано
# print(md2)
# print(md2.popitem())  # вoзвр случайную пару ключ-значение
# print(md2.popitem())
# print(md2.keys())
# print(md2.values())
# print(md2.items())
# print(md2.clear())
LetterNum = 1
for Letter in "Привет":
    if Letter == "и":
        pass
        print("Haйдeнo и, не обработано.")
    print("Бyквa ", LetterNum, " будет ", Letter)
    LetterNum += 1
