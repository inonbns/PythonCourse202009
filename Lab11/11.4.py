
while True:
    from random import randint
    x = int(randint(1, 1000000))
    if (x % 7 == 0) and (x % 13 == 0) and (x % 15 == 0):break
print(x)

"""
Uri's comments:
==============

* Very good! This code works.
* You don't need to have empty lines in the beginning of the file.
  (PyCharm's Code -> Reformat Code feature will delete them).
* It's possible to import things from the middle of the file and it works,
  however if possible it's common to write the imports at the beginning
  of the file. Unless there is some conflict with the imports,
  and then you can write the import inside a function or method.
   
"""
