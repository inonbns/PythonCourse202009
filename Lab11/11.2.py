
while True:
    try:
        age = int(input("insert your age"))
        break
    except:
        input("try again")
print("your age in months is",  age*12)

"""
Uri's comments:
==============

* This code works if there is no exception, but input("try again") doesn't do 
  anything with the input. It's better to use print.

"""
