multiples_of_4 = [num for num in range(11) if num % 4 == 0]
print("List of multiples of 4:", multiples_of_4)
multiples_of_2 = []
for num in multiples_of_4:
    multiples_of_2.append(num // 2)
print("List of multiples of 2:", multiples_of_2)
half_values = multiples_of_2[:]
for i in range(len(half_values)):
    half_values[i] = half_values[i] // 2
print("List of numbers after dividing by 2 againn:", half_values)

#Output 
#List of multiples of 4: [0, 4, 8]
#List of multiples of 2: [0, 2, 4]
#List of numbers after dividing by 2 againn: [0, 1, 2]