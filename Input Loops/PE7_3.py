total_sum = 0
number = 1
while number <= 100:
    if number % 2 == 0:
        total_sum += number
    number += 1
print(f"Sum = {total_sum}")
