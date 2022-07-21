a = abs(10) + abs(-10)
print(a)
b = abs(-10) + -10
print(b)
a = '''этот если способ вы плохо это подходит читаете для что-то 
шифрования пошло важных не сообщений так'''
b = a.split()
# for i in range(0, len(a), 2):
#   print(b[i])

f = open('C:\\Users\\DESKTOP-65L32PF\\Desktop\\Program\\test.txt')
d = f.read()
print(d)
f.close()
f = open('C:\\Users\\DESKTOP-65L32PF\\Desktop\\Program\\test2.txt', 'w')
f.write(d)
f.close()
