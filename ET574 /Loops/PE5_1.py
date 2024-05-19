#A
a = list(range(5))
print(a)

#Output of A
#print("""
   #   [0, 1, 2, 3, 4] """)

#B 
b = []
for i in range (5):
 b.append(i)
print(b)

#Output of B
#[0, 1, 2, 3, 4]

#C
x = list(range(-10, 10))
print(x)
print(min(x), max(x), sum(x))

#Output of C
#[-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#-10 9 -10

#D
even_num = list(range(2, 11, 2)) 
print(even_num[0], even_num[-1])

#Output of D
#2 10

#E
odd_num = [num for num in range(1, 10) if num % 2 != 0]
print(odd_num)
#Output of E
#[1, 3, 5, 7, 9]

#F
cubes = [num ** 3 for num in range(1, 11)]
for cube in cubes:
    print(cube)
#Output of F
#1
#8
#27
#64
#125
#216
#343
#512
#729
#1000
    
#G
cubes = [num ** 3 for num in range(1, 11)]
print('|'.join(str(cube) for cube in cubes))
#1|8|27|64|125|216|343|512|729|1000



