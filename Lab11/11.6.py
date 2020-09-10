
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

"""
Uri's comments:
==============

* If you want the user to guess the number, don't print it.
* The messages you printed are opposite - for example "המספר גדול מדי"
  if the number is too small. Please try again.
   
"""
