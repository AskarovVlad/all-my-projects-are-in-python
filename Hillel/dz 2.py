s = 'qwertey-bgtbttr e'
a = s.replace('e', 'A', 2)
print(a)
print(s.endswith('tre'))
b = ['1', '2', '3', '4', '5']
c = "-".join(b)
print(c)
x = s.expandtabs()
print(x)
print(ord('D'))
x = True
y = False
z = False
if not x or y:
    print(1)
elif not x or not y and z:
    print(2)
elif not x or y or not y and x:
    print(3)
else:
    print(4)

import random

d = random.random()
print(abs(d) > 1)
print(type(1 / 2))
a = [1, 2, 3, None, (), [], ]
print(len(a))
for el in a:
    print(el)
a = 5
print(12 < a < -12)
a = [6, 5, 4, 3, 2, 1]
g = (1, 2, 3, 4, 5, 6)
a[2] = g[3]
print(g[1:3])
a = range(9)
b = range(6)
print(type(a))
print(b[1])
