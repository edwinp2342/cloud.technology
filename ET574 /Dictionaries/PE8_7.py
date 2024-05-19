#7
letters=[]
for i in range(26):
    letters.append(chr(i+97))
numbers=[]
for i in range(1,27):
    numbers.append(i)
charNum=dict(zip(letters,numbers))
for i in charNum:
    print(i,charNum[i],end='|')
    
#7b) 
print()
letters=[]
for i in range(26):
    letters.append(chr(i+97))
numbers=[]
for i in range(100,2601,100):
    numbers.append(i)
numChar=dict(zip(numbers,letters))
for i in numChar:
    print(i,numChar[i],end='|')
print()
all=charNum
all.update(numChar)
print(all)