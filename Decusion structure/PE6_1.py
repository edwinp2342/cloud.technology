#A
print(2 ** 3 == 0 ** 2)
#Output of A
#False

#B
print(2 < 3 or 3 < 2)
#Output of B
# True

#C
print('dog' > 'cat' + 'mouse')
#Output of C
#True

#D
print('Car' < 'Train')
#Output of D
#True

#E
print((2 == 3) and ((2 * 3 < 3 * 3) or (3 < 2) and (2 * 2 < 3)))
#Output of E 
#False

#F
print((2 <= 3) or ((2 * 2 < 3 * 3) or (3 < 2) and (2 * 2 < 3)))\
#Output of F
#True

#G
print(not ((2 < 3) and (2 < (3 + 2))))
#Output of G
#False

#H
print("small" > "large" and (not 3 ))
#Output of H
#False

#I
print(isinstance(3, int)) 
#Output of I
#True

#J
print(isinstance(3.14, float))
#Output of J
#True

#K
if (2 < 3 < 0):
    b = 3+ 2
else:
    b  = 0 * 2
print(b)
#Output of K
#0???

#L
if ('A' in 'apple'):
 print("A as apple." )
else:
 print('Oops, not there.')
 #Output of L
 #Oops, not there.

 #M
 x = 6
if (x < 0):
 print('negative')
else:
 if (x == 0):
 print('zero')
else:
print('positive')

