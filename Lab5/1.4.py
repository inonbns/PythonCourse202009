x= int(input("הכנס מספר"))
if (x%7==0) or ('7' in str(x)) :
    print(f"{x} is boom")

"""
Uri's comments:
==============

* Very good! This code works.
* It's better to add a space in the input after "הכנס מספר", so that the user's
  input will be separated from the last word of the input.
  This is relevant to all your exercises.
* I recommend styling your code according to PEP-8. You can also use PyCharm's
  Code -> Reformat Code feature. For example, spaces around "=" and "==".
  This is relevant to all your exercises.
* Here is how your code looks reformatted:

x = int(input("הכנס מספר: "))
if (x % 7 == 0) or ('7' in str(x)):
    print(f"{x} is boom")

"""
