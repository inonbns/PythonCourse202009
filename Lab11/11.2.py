
while True:
    try:
        age = int(input("insert your age"))
        break
    except:
        input("try again")
print("your age in months is",  age*12)
