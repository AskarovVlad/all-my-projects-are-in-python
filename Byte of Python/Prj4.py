# a = ['first', 1, 2, 3, 'second', 4, 5, 6, 7, 8, 'third', 9, 10]
# my_dict = {}
# current_str = None
# for element in a:
#     if type(element) == str:
#         my_dict[element] = []
#         current_str = element
#     else:
#         my_dict[current_str].append(element)
# print(my_dict)
# b = 'Hello world i like Python and i love Lesia'
# my_dict2 = {}
# for word in b.split():
#     if word in my_dict2:
#         my_dict2[word] += 1
#     else:
#         my_dict2[word] = 1
# print(my_dict2)
# my_dict3 = {}
# for word in b.split():
#     my_dict3[word] = my_dict3.get(word, 0) + 1
# print(my_dict3)
#
x = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
print(x[1][1])
for arr in x:
    for el in arr:
        print(el, end=' ')
    print()
# x[1][1] = 100
# for el in range(len(x)):
#     for el2 in range(len(x[el])):
#         print(x[el][el2], end=' ')
#     print()
# a = [0, 1, 2, 3, 4, 5]
# b = [num * 2 for num in a]
# print(b)

#
# def create_array(m, n):
#     for el in range(n):
#         print('0 ' * m)
#
# print(create_array(10, 6))
# c = [el * 3 for el in range(10)]
# print(c)
a = [20, 18, 16, 14, 12, 10, 8, 6, 4, 2, 0]
b = [num * 2 for num in range(10, 0, -2)]
print(b)
