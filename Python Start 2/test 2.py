def weight(weighte, weightn, x):
    x += 1
    for y in range(1, x):
        weightm = (weighte + weightn * y) * 0.165
        print("%s Год. Вес становит: %s кг" % (y, weightm))


weight(35, 0.3, 5)

# n = 52
# m = True
# while m:
#     guess = int(input("Enter the number:\n"))
#     if guess == n:
#         print('You win')
#         break
#     else:
#         print("Try again")
# print('The end')

list1 = []
for i in range(1, 10):
    print(i)
    if i >= 2:
        continue

x = 150
y = 250


def func(x, y=100):
    print(x + y)


func(100, 1000)
func(100)


def func2(a=5, *numbers, **phonebook):  # * собирает все значения в кортеж, ** в словарь
    print('a', a)
    # проход по всем элементам кортежа
    for single_item in numbers:
        print('single_item', single_item)
    # проход по всем элементам словаря
    for key, value in phonebook.items():
        print(key, value)


print(func2(555, 1, 2, 3, Jack=1123, John=2231, Inge=1560))


def total(initial=5, *numbers, extra_number=50):
    count = initial
    for number in numbers:
        count += number
    count += extra_number
    print(count)


total(10, 1, 2, 3, 150)
total(999, 1, 2, 3)


def func3(x, y):
    '''Первая строка название с заглавной буквы , вторая пустая

третья подробное описание и точка. '''
    return x + y


print(func3(1, 3))
print(func3.__doc__)
x = 3
print(id(x))
