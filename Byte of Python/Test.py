def my_func(num):
    if num % 2 == 0:
        print(f'число {num} чётное')
    else:
        print(f'число {num} не чётное')
my_func(10)

print(round(2.007, 2))
print(int(2.7))
print("""№кбпазук#""")

my_string = 'i like Dota2'
my_string = my_string.replace('Dota2', 'Ptn')
print(my_string)
print(my_string.title())
# my_string = "-".join(my_string)
# print(my_string)
my_string1 = 'I ' + "like " + "Python"
print(my_string1)
print(my_string.split(" "))
print(id(my_string))
print(type(my_string))
numb = 9379992
numb1 = 13.515
print(type(numb))
print(type(numb1))
my_string2 = ['i', 'like', 'Ptn']
print("-".join(my_string2))
x = "I like Python        "
print(x)
x = x.strip()   # обрезать, () - что обрезать в "", sltrip - слева обрезать, rstrip - справа
print(x)
