my_list = ['qwe', 'er', 'tye', 'as', 'dfe']
up_list = []
for el in my_list:
    up_list.append(el.upper())
print(up_list)
up_list2 = []
for index in range(len(my_list)):
    if not index % 2:
        up_list2.append(my_list[index].upper())
    else:
        up_list2.append(my_list[index])
print(up_list2)
up_list3 = []
for index in range(len(my_list)):
    element = my_list[index]
    if element == 'as':
        break
    elif len(element) == 2:
        continue
    else:
        up_list3.append(element.upper())
print(up_list3)
list_int = [1, 2, 3, 4, 5]
list_int5 = []
for el in list_int:
    el += 5
    list_int5.append(el)
print(list_int5)
print('2)  ##################################################')
lst = ['zxc', 'vb', 'nm', 'lkj', 'hgf']
for index, value in enumerate(lst):
    if not index % 2:
        print(value)
a = enumerate(lst)
b = next(a)
print(b)
print('3)  ##################################################')
# Дана строка My name is Vova. I'm 41. But I still believe in magic. EXPELLIARMUS!
# 1 Составить строку из больших букв этого предложения
# 2 Составить строку из маленьких букв этого предложения
# 3 Составить строку из больших гласных букв этого предложения
# 4 Составить строку из маленьких согласных букв этого предложения
# 5 Составить строку из букв этого предложения, заменив большие буквы на маленькие и наоборот
# 6 Составить строку из символов этого предложения по следующему правилу:
# 7 Большие буквы в алфавитном порядке. Затем маленькие гласные буквы в алфавитном порядке.
# 8 Потом маленькие согласные буквы в алфавитном порядке.
# 9 Затем другие символы в порядке, в котором они есть в предложении.
my_str = "My name is Vova. I'm 41. But I still believe in magic. EXPELLIARMUS!"
new_str = []
for el in my_str:
    if el.isupper():
        new_str.append(el)
new_str = "".join(new_str)
print(new_str)
print('4 ##################################################')
new_str1 = []
for el in my_str:
    if el.islower():
        new_str1.append(el)
new_str1 = "".join(new_str1)
print(new_str1)
print('5 ##################################################')
print(my_str.swapcase())
print('6 - 9 ##################################################')
some_string = "My name is Vova. I'm 41. But I still believe in magic. EXPELLIARMUS!"
new_str2 = []
big_letter = []
small_a = []
small_b = []
symbols = []
for symbol in some_string:
    if symbol.isupper():
        big_letter.append(symbol)
    elif symbol in "eyuioa":
        small_a.append(symbol)
    elif symbol.isalpha():
        small_b.append(symbol)
    else:
        symbols.append(symbol)
result = sorted(big_letter) + sorted(small_a) + sorted(small_b) + symbols
result_str = "".join(result)
print(result_str)
# Посчитать все элементы списка, сколько каждый
lst = [0, 1, 2, 2, 3, 3, 3, 3, 4]
print(len(lst))
print(lst.count(0), lst.count(2))
my_dict = {el: lst.count(el) for el in lst}
print(my_dict)
