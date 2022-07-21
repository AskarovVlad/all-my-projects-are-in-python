a = -3
print(abs(a))
b = 1
print(bool(abs(a) > b))

print(5 * 10)
my_small_program = '''print('бутерброд')
print('с колбасой')
print('gus')'''
exec(my_small_program)
x = 10 - 1
print("%.100f" % x)
print(float("{0:.10f}".format(x)))
z = ['0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000']
print(len(z))
string = 'БабА'
print(max(string))
print(min(1, 2, 3, -10, 0))
my_number = 61
my_friends_number = [1, 10, 100]
if max(my_friends_number) > my_number:
    print('You win')
else:
    print('I win')
test_file = open('C:\\Users\\DESKTOP-65L32PF\\Desktop\\Program\\test.txt')
text = test_file.read()
print(text)
