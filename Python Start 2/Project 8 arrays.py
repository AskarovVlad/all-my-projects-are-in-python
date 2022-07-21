a = [1, 2, 3, 4, 5, "Vlad", "Pishet", "Na ugad"]
for x in range(len(a)):
    print(x, a[x])
    #print(len(a))
print(a[5])
b = [6, 7, 8, 9, "Daleco on ne Uedet"]
a.extend(b)
print(a)
print(len(a))
c = a + b
print(c)
