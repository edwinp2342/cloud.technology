range_end=int(input("enter a range"))
numbers= list(range(1, range_end + 1))
multipler=int(input("Enter the integer number"))
for number in numbers:
    print(f"{number}*{multipler}={number*multipler}")

    #Output+enter a range6
#Enter the integer number6
#1*6=6
#2*6=12
#3*6=18
#4*6=24
#5*6=30
#6*6=36