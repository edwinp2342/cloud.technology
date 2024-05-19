import math
while True:
    try:
        numerator = float(input("Enter a numerator: "))
        denominator = float(input("Enter a denominator: "))
        if denominator == 0:
            print("Denominator cannot be zero. Try again.")
            continue
        result = math.fmod(numerator, denominator)
        print(f"{int(numerator)} mod {int(denominator)} = {int(result)}")
        break
    except ValueError:
        print("Please enter valid numbers.")
