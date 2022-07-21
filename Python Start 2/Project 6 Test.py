for x in range(0, 20):
    print("Privet %s" % x)
    if x >= 4:
        break

for x in range(1, 25, 2):
    print(x)

ingredients = ['слизни', 'пиявки', 'катышки из пупка гориллы', 'брови гусеницы', 'пальцы многоножки']
x = 0
for y in ingredients:
    x += 1
    print("%s %s" % (x, y))

y = 0
for x in range(1, 26):
    if x % 3 == 0:
        y += 1
print(y)
