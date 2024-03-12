multiples_of_four=[x*4 for x in range(11)]
print(multiples_of_four)
h=[]
for number in multiples_of_four:
    h .append(number/2)
print(h)
third_list=h[:]
for i in range(len(third_list)):
    third_list[i]/=2

    #Output=[0, 4, 8, 12, 16, 20, 24, 28, 32, 36, 40]
#[0.0, 2.0, 4.0, 6.0, 8.0, 10.0, 12.0, 14.0, 16.0, 18.0, 20.0]