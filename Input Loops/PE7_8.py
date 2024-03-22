n1 = int(input("Enter the first number (n1): "))
n2 = int(input("Enter the second number (n2): "))
if n1 < n2:
    for number in range(n1, n2 + 1):
        print(number, end=' ')
elif n1 > n2:
    for number in range(n1, n2 - 1, -1):
        print(number, end=' ')
else:
    print("n1 = n2")
