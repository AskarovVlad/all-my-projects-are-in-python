a = [1, 2, 3, 4, 5, 'hello', 'world', 'I', 'like', 'Python', 'hello', 1, 2, 3, 4, 5, 'I']
print(a)
a.append(6)  # добавить значение в список
print(a)
b = set()  # создать пустое множество можно только так
for el in a:
    b.add(el)  # добавить значение в множество только так
print(len(a))
print(b)
print(len(b))
c = set(a)
print(c)
d = list(c)
print(d)
print(5 in c)
print(15 not in c)
x = [1, 1, 1, 2, 2, 3, 3, 4, 5, 6, 7, 8, 9, 9, 9]
y = set(x)
print(y)
sum_el = 0
for el in y:
    sum_el = el + sum_el
print(sum_el)
print(sum(y)) # функция суммирует списки, множества и тд
print(sum(set(x)))
