# x = 1
# y = 1
# print(' ' * 4, end=' ')
# for x in range(1, 11):
#     print(f'{x:>4}', end=" ")
# print()
# for x in range(1, 11):
#     print(f'{x:>4}', end=" ")
#     while y <= 10:
#         print(f'{x * y:>4}', end=" ")
#         y += 1
#     print()
#     y = 1

def filter_string(string, char):
    result = ''
    for element in string:
        if char.upper() != element.upper():
            result += element
    print(result)

filter_string('If I look forward I am win', 'I')


# def reverse(string):
#     result = ''
#     for char in string:
#         print(char)
#         result = char + result
#     return result
#
#
# print(reverse('go!'))  # '!og'
