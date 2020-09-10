import math
from random import randint
print("מספר ראשון")
x= int(randint(1, 10))
print(x)
print("מספר שני")
y = int(randint(1, 10))
print(y)


print(math.gcd(x,y))

"""
Uri's comments:
==============

* It's good you used math.gcd, however the math.gcd result is not the expected
  result of the assignment. You can use it to calculate the result. Please try again.
   
"""
