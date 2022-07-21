num: int = 600851475143
d = 2
while d ** 2 <= num:
    if num % d == 0:
        num //= d
    else:
        d += 1
print(num)
print(600851475143 / 6857)
