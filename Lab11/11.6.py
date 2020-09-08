
from random import randint
num_guess = (randint(1, 10))
print(num_guess)

num_user = int(input("בחר מספר"))
while num_user != num_guess:
    if num_guess > num_user:
        print("המספר גדול מדי")
        num_user = int(input("בחר מספר"))
    else:
        print("המספר קטן מדי")
        num_user = int(input("בחר מספר"))
print(f"{num_guess}הצלחת המספר הוא ")
