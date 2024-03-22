numbers = []
while True:
    num = float(input("Enter a number or 0 to stop: "))
    if num == 0:
        break  
    numbers.append(num)
total_sum = sum(numbers)
average = total_sum / len(numbers) if numbers else 0
print(f"Sum = {total_sum}")
print(f"Average = {average}")
print(f"Number(s) entered: {' '.join(map(str, numbers))}")
