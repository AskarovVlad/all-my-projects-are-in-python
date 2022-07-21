num = 1000
my_list = list(range(1, 11))
for el in my_list:
    if num % el != 0:
        num += 10
        continue
    else:
        print(num)
