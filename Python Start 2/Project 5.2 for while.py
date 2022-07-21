words = ["apple", "banana", "computer", "music", "stop", "these", "words", "will", "not", "be", "printed"]

    # Задание 2 (с помощью цикла while)
# i2 = 0
    # Итерируем, пока не наткнемся на слово "stop"
#while words[i2] != "stop":
#    print(words[i2])
#    i2 += 1


for i in range(len(words)):
    if words[i] == "stop":
        break

    print(words[i])
