#A
fruits = ["apple", "pear", 'python']
for item in fruits: 
    print(f"{item.title()} is my favorite!")
    print(f"I want to have more {item}.\n")

#Explaination: uses the title() to capitalize the first letter of each string/fruit.

#B
numbers = [12345]
for n in numbers: 
    print(n) 
    print("That’s all the numbers in the list.")
print("numbers = ", numbers)

#Explaination: Loop over a list which contains a single integer.

#C
n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
count = 0
for i in n: 
    print(i, end = '\t')
    count += 1
print(f"\nThere are {count} numbers in the list.")
print("n = ", n)

#Explaination: Using loop control  and concatenation of string output with tab separation.

#D
languages = ["c++", "java", "python"]
for code in languages: 
    print(code.upper(), end = " | ")
else: 
    print("Enjoy coding!")

#Explaination: else block executes after the loop completes, showing how else works with loops.

#E
n = [-6, 7, 3, -2, 6, 3, 9]
print(len(n), max(n), min(n), sum(n), sep = '\n')
print(n.count(3), n.index(3), n[-6:6], sep = '\n')
print(n, sorted(n), sep = '\n')

#Explaination: Examples of len(), max(), min(), sum(), count(), index(), and list slicing. Also showing the sorting of a list.

#F
a = 2
b = 3
print(type(a+b))
print(type((a+b)))
print(type(()))

#Explaination: Demonstrating how the type() function is used. 