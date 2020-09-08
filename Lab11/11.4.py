
while True:
    from random import randint
    x = int(randint(1, 1000000))
    if (x % 7 == 0) and (x % 13 == 0) and (x % 15 == 0):break
print(x)
