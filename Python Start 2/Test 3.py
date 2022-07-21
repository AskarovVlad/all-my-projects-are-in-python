import sys


def weight():
    print("Какой Ваш вес?")
    weighte = int(sys.stdin.readline())
    print("Какой ежегодный прирост веса?")
    weightn = int(sys.stdin.readline())
    print("Сколько лет?")
    age = int(sys.stdin.readline())
    age += 1
    for x in range(1, age):
        weightm = (weighte + weightn * x) * 0.1
        print("%s Год. Вес становит: %s кг" % (x, weightm))
weight()
