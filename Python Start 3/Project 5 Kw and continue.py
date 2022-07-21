import keyword
import time

print(keyword.kwlist)

a = ['banana', 'orange', 'lemon', 'bread', 'box', 'cucumber']
for eat in a:
    if eat.startswith('b'):
        continue
    print(eat)
import random

print(random.randint(0, 10))
random.shuffle(a)  # перетасовка
print(a)

import sys

sys.stdout.write("0123456789")


def numbers(max):
    t1 = time.time()
    for x in range(0, max):
        print(x)
    t2 = time.time()
    print('Прошло %s секунд' % (t2 - t1))


numbers(10)


t = (2021, 8, 25, 19, 34, 30, 3, 0, 0)

import time
print(time.asctime(t))
