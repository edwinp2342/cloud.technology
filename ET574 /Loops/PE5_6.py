#Given Code A
#fruits = ["apple" "banana" "cherry"]
#for item in fruits
#print(item)

#Corrected 
fruits = ["apple", "banana", "cherry"]
for item in fruits:
    print(item)

#Given Code B
#for i in range (1 4):
#print(i + '\t' + 2**i)

#Corrected 
for i in range(1, 4):
    print(str(i) + '\t' + str(2**i))

#Given Code C
#for j in range (1 6 -1):
#print(j)

#Corrected 
for j in range(5, 0, -1):
    print(j)

#Given Code D
#letters = ['a' 'b' 'c']
#for letter in letters: 
#letter = letter.upper()
#print(letters)

#Corrected 
letters = ['a', 'b', 'c']
for letter in letters: 
    print(letter.upper())

#Given Code E
#fruits = ('apple' 'banana' 'cherry')
#print(fruits) 
#fruits[0] = 'orange' 
#fruits.append('pineapple')
#print(fruits)

#Correction 
fruits = ['apple', 'banana', 'cherry']
print(fruits) 
fruits[0] = 'orange'
fruits.append('pineapple')
print(fruits)







