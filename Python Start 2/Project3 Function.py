def function4(name, surname, age):
    fio = f'{name}'
    print(fio)
    if age < 18:
        return "111111"
    elif age == 18:
        return "222222"
    else:
        return "333333"


fio1 = function4("Vlad", "Askarov", 25)
print(fio1)
