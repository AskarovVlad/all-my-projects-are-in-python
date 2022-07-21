words = ["computer", "music", "stop", "these"]
# x = 0


# while words[x] != "stop":
#    print(words[x])
#    x += 1


for h in range(len(words) - 1, -1, -1):
    if words[h] == "stop":
        break

    print(words[h])

for x in range(len(words)):
    for y in range(x+1):
        print(words[x])
