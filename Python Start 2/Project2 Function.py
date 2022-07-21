def function3(name, height, weight):
    bmi = weight / (height ** 2)
    print("Индекс масы тела:  " + str(bmi))
    if bmi < 25:
        return name + " net lishnego vesa"
    elif bmi == 25:
        return name + " vse horosho"
    else:
        return name + " yest lishniy ves"
bmi1 = function3("vlad", 1.73, 67)
print(bmi1)

a = pow(2, 2)
print(a)
