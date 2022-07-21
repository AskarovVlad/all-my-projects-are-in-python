import time

print(time.asctime())

import sys


def silly_age_joke():
    print('Сколько вам лет?')
    age = int(sys.stdin.readline())
    if 10 <= age <= 15:
        print('13 + 49 + 84 + 155 + 97: что получится? Головная боль!')
    else:
        print('Что-что?')


silly_age_joke()
