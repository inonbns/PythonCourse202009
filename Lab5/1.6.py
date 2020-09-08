num1 = int(input("הכניסו איבר ראשון בסידרה חשבונאית"))
diff = int(input("הכניסו הפרש בסידרה חשבונאית"))
n = int(input("הכניסו מספר איברים בסידרה חשבונאית"))

numn = num1 + diff*(n-1)
Sum = diff*(num1+numn)/2
print(f"Sum is {Sum}")