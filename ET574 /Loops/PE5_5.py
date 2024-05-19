range_end = int(input("Enter the range end for the multiplication table: "))
numbers = list(range(1, range_end + 1))
multiplication_number = int(input("Enter the number for which you want the multiplication table: "))
print(f"Multiplication table of {multiplication_number}:")
for num in numbers:
    print(f"{multiplication_number} x {num} = {multiplication_number * num}")

#Output
#Multiplication table of 2:
#2 x 1 = 2
#2 x 2 = 4