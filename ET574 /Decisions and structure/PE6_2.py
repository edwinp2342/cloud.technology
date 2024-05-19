age = int(input("Enter your age: "))
if age < 0:
    print("Invalid age!!!!")
elif age < 2:
    print("Youre a baby!")
elif age < 4:
    print("Youre a toddler!")
elif age < 13:
    print("Youre a kid!")
elif age < 20:
    print("Youre a teenage!")
elif age < 65:
    print("Youre am adult!")
else:
    print("Youre a elder!")
