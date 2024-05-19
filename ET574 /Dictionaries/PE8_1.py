NY = {"BX":1.42, "MN":1.63, "QS":2.25, "BN":2.56, "SI": 0.47}

#A
print((NY['QS']))
print(NY.get("QS"))

#Output of A
#2.25
#2.25

#B
print(NY.get("LI", "Not in"))
print(NY.get('SI', 'absent'))
print(NY.setdefault('SI', 0.48))

#Output of B
#Not in
#0.47
#0.47

#C
print("LI" in NY)
print('MN' not in NY)

#Output of C
#False
#False

#D
print(len(NY), min(NY), max(NY))
print(len(NY.items()),
max(NY.keys()), min(NY.values()))

#Output of D
#5 BN SI
#5 SI 0.47

#E
print(round(NY['QS']))
NY['QS'] += .3
print(round(NY['QS'], 1))

#Output of E 
#2
#2.5

#F
print(NY.keys())
print(list(NY.values()))
print(tuple(NY.items()))

#Output of F
#dict_keys(['BX', 'MN', 'QS', 'BN', 'SI'])
#[1.42, 1.63, 2.55, 2.56, 0.47]
#(('BX', 1.42), ('MN', 1.63), ('QS', 2.55), ('BN', 2.56), ('SI', 0.47))

#G
total = 0
for x in NY.values():
    total += x
print(f'{total:.1f}')

#Output of G
#8.6

#H
total = 0
for x in NY:
    total += NY[x]
print(f'{total:.1f}')

#Output of H
#8.6