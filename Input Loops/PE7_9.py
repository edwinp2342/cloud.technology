lower = int(input("Enter the lower bound: "))
upper = int(input("Enter the upper bound: "))
incVal = int(input("Enter the increment value: "))
current = lower
print("Values with while loop:")
while current <= upper:
    print(current)
    current += incVal
current = lower
print("All values in increments using while loop:")
while current <= upper:
    inner = current
    while inner < current + incVal and inner <= upper:
        print(inner)
        inner += 1
    current += incVal
print("All values in increments using for loop:")
for current in range(lower, upper + 1, incVal):
    for inner in range(current, min(current + incVal, upper + 1)):
        print(inner)
