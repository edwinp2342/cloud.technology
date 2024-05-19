n = int(input("Enter a positive number: "))
if n > 0:
    print(f"Range = 1 to {n}")
    for number in range(1, n + 1):
        if number % 2 != 0 and number % 5 == 0:
            print(number, end=' ')
else:
    print("Invalid input.")
