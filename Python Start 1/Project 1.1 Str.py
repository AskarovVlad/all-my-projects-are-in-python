gender = {'m': "Дорогой", "f": "Дорогая"}
people = [['Семен', "Синяков", 132, "m"],
          ['Клара', "Егорова", 55138, "f"],
          ['Лариса', "Нескажу", 99134, "f"]]
for name, surname, balance, g in people:
    messenger = f'''{gender[g]} {name} {surname}, ваш баланс составляет {balance} гривен.
Вам стоит начать экономить.'''
    print(messenger)
s = [1, 2, 3, 4, 5, -10]
print(s)
s1 = sorted(s, reverse=True)
print(s1)
s2 = sorted(s)
print(s2)
