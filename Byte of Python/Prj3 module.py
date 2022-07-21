# import math
# print(int(math.sqrt(25)))
# print(math.pi)
#
# import sys
# print(sys.path)

# import math
#
# print(dir(math))
# print(dir())
import copy  # копирование
import keyword  # ключ
import random  # рандомные числа
from datetime import *  # модуль времени


class Auto:
    pass


my_auto1 = Auto
my_auto1.wheels = 4
my_auto2 = copy.copy(my_auto1)
my_auto2.wheels = 8

print(my_auto1.wheels)
print(my_auto2.wheels)

s = ['audi', 'bmw', 'toyota']
print(keyword.iskeyword('is'))
print(random.randint(0, 10))
print(random.choice(s))
print(time(t))
