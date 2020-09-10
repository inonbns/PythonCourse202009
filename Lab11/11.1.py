max = 0

for i in range(3):
    num = int(input("הכנס מספר"))
    if max>num:
        max=max
    else:
        max=num
print(f"max is {max}")

"""
Uri's comments:
==============

* Very good! This code works.
* Notice that all the numbers might be negative:

        הכנס מספר -1
        הכנס מספר -2
        הכנס מספר -3
        max is 0

  In python you can use float("-inf") to create the smallest possible value,
  so I would write:

        big_num = float("-inf")

* Python has the function "max", and it's better to use it than implementing
  your own solution. You don't have to "invent the wheel" each time again.
  Built-in Functions in Python: https://docs.python.org/3/library/functions.html
* max is a built-in function in Python and although you can, it's not recommended
  to use it as a name of a variable.
  PyCharm warns about it (you can see a line under "max" which you can hover and 
  see the full warning).

"""
