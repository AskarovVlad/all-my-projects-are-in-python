list = [1, 2, 3, 4, -1, -2, -3, -4, -5, -7, -8]
total = 0
x = len(list) - 1
while x >= 0 and list[x] < 0:
    total += list[x]
    x -= 1
print(total)

total2 = 0
for y in range(len(list) - 1, -1, -1):
    if list[y] > 0:
        break

    total2 += list[y]
print(total2)

list2 = [1, 1, 2, 3, 3, 5, 10]
total1 = 0
y = 0
while y < len(list2) and total1 < 10:
    total1 += list2[y]
    y += 1
print(total1)
