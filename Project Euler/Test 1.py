y = 0
for x in range(0, 10):
    if x % 3 == 0 or x % 5 == 0:
        print(x)
        y += x
print(y)
for x in range(0, 10):
    print(x, end=' ')
