#Given code for A 
str0 = "py"
print(str0[0])
print(str0[-1])
print(str0[:])
print(str0[0], str0[-1], 
str0[:], sep = ' ')

#Output of A
print("""p
y
py
p y py""")
#Explaination of A

#Given code for B 
print('C'[0])
print("C"[-1])
print('C'[:])
print('C'[0], 'C'[-1],
'C'[:], sep = '\t')
 
#Output of B
print(""" 
C
C
C
C       C       C""")
#Explaination of B


#Given code for C 
str1 = "coDE"
print(str1.capitalize()+'\n'+str1.upper()+'\n'+str1.lower())
print(str1)

#Output of A
print("""
 Code
CODE
code
coDE""")

#Explaination of C


#Given code for D 
str2 = "computer science"
print(str2.title(),'|',str2[0:8],'|',str2[:3],'|',
str2[-5:-1], '|', str2[-2:] )
print(str2.title(), str2[0:8], str2[:3],
str2[-5:-1], str2[-2:], sep = ' | ')

#Output of D
print("""Computer Science | computer | com | ienc | ce
Computer Science | computer | com | ienc | ce """)

#Explaination of D: 

#Given code for E 
str3 = "mississippi"
print("i =",str3.count('i'))
print("s = index[", str3.find('s'), ']')
print('p = ', str3.rfind('p'))
print("Miss = ", str3.find("Miss"))

#Output of E
print("""
i = 4
s = index[ 2 ]
p =  9
Miss =  -1 """)

#Explaination of E: 

#Given code for F 
str4 = " Today's program "
print('lstrip():',str4.lstrip())
print('rstrip():',str4.rstrip())
print('strip():',str4.strip() + " – Basic IO")

#Output of F
print("""
lstrip(): Today's program
rstrip():  Today's program
strip(): Today's program – Basic IO """)

#Explaination of F: 

#Given code for G
print("Price: ", '$', 19.99)
print("Price: ", '$', 19.99, sep = '')

#Output of G
print("""
 Price:  $ 19.99
Price: $19.99""")

#Explaination of G: 

#Given code for H 
print('Py', 'th', 'on', sep = '')
print('Py', 'th', 'on', sep = '\t')
print('Py', 'th', 'on', sep = '\n')

#Output of H
print("""
 Python
Py      th      on
Py
th
on""")

#Explaination of H


#Given code for I 
print('tic', 'tac', 'toe', sep = '-', end = ' ')
print("game starts", end = '!\n')
print('in'.title(), 'person'.capitalize(), sep = '-', end = ' ')
print('tutoring'.upper())

#Output of I
print("""
tic-tac-toe game starts!
In-Person TUTORING """)

#Explaination of I: 


#Given code for J 
print("Number\tSquare")
print(str(2) + '\t' + str(2**2))
print(str(3) + '\t' + str(3**2))
print(2, '\t', 2**2)
print(3, '\t', 3**2)

#Output of J
print("""
 Number  Square
2       4
3       9
2        4
3        9""")

#Explaination of J: 


#Given code for K
print("STATE\tCAPITAL".expandtabs(15))
print('North Dakota\tBismarck'.expandtabs(15))
print('South Dakota\tPierre'.expandtabs(15))
print('Ohio\tColumbus'.expandtabs(15))
print('North Dakota\tBismarck')
print('South Dakota\tPierre')
print('Ohio\tColumbus')

#Output of K
print("""
STATE          CAPITAL
North Dakota   Bismarck
South Dakota   Pierre
Ohio           Columbus
North Dakota    Bismarck
South Dakota    Pierre
Ohio    Columbus """)

#Explaination of K: Using \T provides space between the States and (15) adjust how much space in given.



