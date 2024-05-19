even_numbers = [num for num in range(101) if num % 2 == 0]
first_five_even = even_numbers[:5]
print(f"First five even numbers: {first_five_even}")
last_five_even = even_numbers[-5:]
print(f"Last five even numbers: {last_five_even}")
even_20_to_30 = even_numbers[10:16]  # Assuming the list starts at 0, the 20th even number is at index 10, and 30 is at 15
print(f"Even numbers from 20 to 30: {even_20_to_30}")

#Output 
#First five even numbers: [0, 2, 4, 6, 8]
#Last five even numbers: [92, 94, 96, 98, 100]
#Even numbers from 20 to 30: [20, 22, 24, 26, 28, 30]
