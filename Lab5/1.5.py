x1 = int(input("הכנס מספר ראשון"))
x2 = int(input("הכנס מספר שני"))
x3 = int(input("הכנס מספר שלישי"))

if (x1>x2) and (x1>x3):
    print(f"{x1}הוא גדול ")
if (x2>x1) and (x2>x3):
    print(f"{x2}הוא גדול ")
else:
    print(f"{x3}הוא גדול ")

"""
Uri's comments:
==============

* I get 2 lines of output in some cases. Please try again.

"""
