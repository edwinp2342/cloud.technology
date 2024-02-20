#Given Code A
print("012345678901234567890")
print('A'.rjust(5), 'B'.center(5), 'C'.ljust(5), sep = "")
#output of A
print("""012345678901234567890
    A  B  C     """)
#Given Code B
print(print("01234567890123456"))
print("{0:^7}{1:4}{2:>6s}".format("one", "two", "three"))
print(f"{'one':^7}{'two':4}{'three':>6s}")

#Output of B
print(""" 01234567890123456
None
  one  two  three
  one  two  three""")

#Given Code C
n=1234
print("01234567890123456789")
print(f"{n:10}{n:^10}")
print("01234567890123456789")
print(f"{n:<10}{n:>10}")
print("01234567890123456789")
print(f"{n:10.3f}{n:10,.2f}{n}")
print("012345678901234567890123456789")
print(f"{n:10.2%}{n:12,.2%}")

#Output of C
print("""      1234   1234
>> 01234567890123456789
>> 1234            1234
>> 01234567890123456789
>>   1234.000  1,234.001234
>> 012345678901234567890123456789
>> 123400.00% 123,400.00%  """)

#Given code D
q1= '''"If {0:s} dream it, {0:s} do it. - Walt Disney"'''
print(q1.format('you can'))
a = 'ONE'
b = 'DAY'
q2 = f"\"{a} {b} or {b} {a}. You decide. Paulo Coelho\""
print(q2)

#Output of D
print("""If you can dream it, you can do it. - Walt Disney"
"ONE DAY or DAY ONE. You decide. Paulo Coelho""")