for x in range(0, 2):
    print("Privet")
for x in range(0, 2):
    print("Privet %s" % x)

wizard_list = ["паучьи лапки", "жабий палец", "глаз тритона", ]
for x in wizard_list:
    print(x)
    for y in wizard_list:
        print(y)

found_coins = 20
magic_coins = 70
stolen_coins = 3
coins = found_coins
for week in range(1, 53):
    coins = coins + magic_coins - stolen_coins
    print('Неделя %s = %s монет' % (week, coins))

x = 10
y = 20
while x < 15 and y < 30:
    x = x + 1
    y = y + 1
    print(x, y)
