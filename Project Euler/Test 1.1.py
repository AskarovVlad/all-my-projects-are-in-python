print('mama ' * 2)
info = "We couldn't verify you mother's maiden name."
intro = "Here is important information about your account security."

first_name = 'Joffrey'
greeting = 'Hello'

# BEGIN (write your solution here)
print(greeting + ", " + first_name + '!')
print(info)
# END
stark = 'Arya'

# BEGIN (write your solution here)
# x = Do you want to eat
template = "{}, {}?"
print(template.format('Do you want to eat', stark))
# END
one = 'Naharis'
two = 'Mormont'
three = 'Sand'

# BEGIN (write your solution here)
template = '{}{}{}{}{}'
print(template.format(one[2], two[1], three[3], two[4], two[2]))
# END
print(pow(2, 3))
print(abs(-100))


def money(zp):
    tax = 0.2 * zp
    print(int(zp - tax))


money(10000)


def sub(a, b):
    resul = a - b
    return resul


print(sub(10, 7))


def sub(a, b):
    # Полученный результат никак не используется
    # и не возвращается наружу
    answer = a - b
    return answer


result = sub(15, 7)
print(result)


def has_targaryen_reference(string):
    n = len(string)
    return string[:n] == "Targaryen"


print(has_targaryen_reference("Targaryen"))


def get_formatted_birthday(day, month, year):
    resultt = "%02d-%02d-%d" % (day, month, year)
    print(resultt)


get_formatted_birthday(30, 2, 1953)


def is_lannister_soldier(color, shield):
    return (color == "red" and shield is None) or shield == "lion"


print(is_lannister_soldier("red", "lio"))


def is_neutral_soldier(color, shield):
    return color != "red" and shield == "black"


print(is_neutral_soldier("red", "black"))


def normalize_url(url):
    if 'https://' in url:
        return url
    else:
        return "https://" + url


print(normalize_url('https://urlee.com'))


def who_is_this_house_to_starks(surname):
    if surname == 'Karstark' or surname == 'Tully':
        return 'friend'
    elif surname == 'Lannister' or surname == 'Frey':
        return 'enemy'
    else:
        return 'neutral'


print(who_is_this_house_to_starks('Lannister'))


def abs(number):
    if number >= 0:
        return number
    return -number


print(abs(-1))


def flip_flop(string):
    return "flip" if string == 'flop' else 'flop'


print(flip_flop('flop'))


def flip_flop(string):
    if string == 'flip':
        return 'flop'
    return 'flip'


print(flip_flop('flip'))


def test_emptiness(string):
    if string:
        return 'non-empty'
    return 'empty'


print(test_emptiness('foo'))  # => 'non-empty'
print(test_emptiness(''))  # => 'empty'


def is_falsy(value):
    return not bool(value)


print(is_falsy(""))


def print_numbers(last_number):
    i = last_number
    while i > 0:
        print(i)
        i -= 1
    print('finished!')


print(print_numbers(3))


def join_numbers_from_range(start, finish):
    join = ""
    i = start
    while i <= finish:
        join = join + str(i)
        i += 1
    return join


print(join_numbers_from_range(0, 8))

def print_name_by_symbol(name):
    i = len(name) - 1
    while i > -1:
        print(name[i])
        i -= 1

print(print_name_by_symbol('name'))
