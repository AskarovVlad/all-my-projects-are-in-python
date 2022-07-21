def count_chars(string, char):
    index = 0
    count = 0
    while index < len(string):
        if string[index] == char.upper() or string[index] == char.lower():
            # Считаем только подходящие символы
            count = count + 1
        # Счётчик увеличивается в любом случае
        index = index + 1
    return count


print(count_chars('jjj rrrA AAAAaa', 'a'))


def reversed_string(string):
    index = len(string) - 1
    reversed_string: str = ''

    while index >= 0:
        current_string = string[index]
        reversed_string = '{}{}'.format(reversed_string, current_string)
        index -= 1

    return reversed_string


print(reversed_string('Game of the Thrones'))


def my_substr(string, index: int, value: int):
    if value == 0:
        return string[0]
    if value == None:
        return None
    if value == " " or value == "":
        return "Error Value"
    if value < 0:
        return 'Error Value, please input value > 0 '
    elif value > len(string) + 1:
        return 'Error_404'
    else:
        return string[index:index + value]


print(my_substr('If_I_look_back_I_am_lost', 2, 10))
my_sub = 'If_I_look_back_I_am_lost'
my_s = my_sub.split("_")
print(my_s)
m = (" ".join(my_s))
print(m)

# def filter_string(text, char):
#     return text = text.replace(char, '')

original = "EXAMPLE"
removed = original.replace("M", "")  # заменять
print(removed)
