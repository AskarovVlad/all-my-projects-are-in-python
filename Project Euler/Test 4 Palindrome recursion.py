# a = range(999, 99, -1)
# b = range(999, 99, -1)
# c = []
# d = []
# for el in a:
#     for element in b:
#         c.append((el * element))
#
# for value in c:
#     value = str(value)
#     if value[:3] == value[-1:2:-1]:
#         d.append(value)
# print(max(d))
def palindrome():
    for x in range(999, 900, -1):
        for y in range(x, 900, -1):
            s = str(x * y)
            c = s[::-1]
            if s == c:
                return c, x, y


print(palindrome())
my_str = 'а роза упала на лапу азора'
my_str1 = ''.join(my_str.split())
if my_str1 == my_str1[-1::-1]:
    print("It's pallindrome:", my_str)
else:
    print("Nooo")


def pal(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return pal(s[1:-1])


print(pal('opopo'))


def rec(l):
    if len(l) == 1 or len(l) == 2:
        return l
    return l[0] + '(' + rec(l[1:-1]) + ')' + l[-1]


# l = input('введите строку: ')
l = 'qwer'
print(rec(l))

a = [1, 2, 3, [11, 22, [111, 222, [3333]]], 4, 5, [11, 22]]


def rec(spisok, level=1):
    print(spisok, 'level=', level)
    for el in spisok:
        if type(el) == list:
            rec(el, level + 1)


rec(a)
m_list = (i for i in range(10))     # выражение генератор
print(list(m_list))
print(list(m_list))
