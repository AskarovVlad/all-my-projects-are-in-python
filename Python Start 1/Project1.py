name = "Tom"
weight = 200
height = 4
bmi = weight / (height ** 2)
# если бми меньше 25, то
print("index масы тела равняется:" + str(bmi))
if bmi < 25:
    print("У " + name + " есть лишний вес")
elif bmi == 25:
    print("У " + name + " what's your name")
else:
    print("\"Тут что-то не так\" - подумал Д'артаньян")
