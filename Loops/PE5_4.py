months=["January", "February", "March", "April", "May", "June" "July", "August", "September", "Octuber", "November", "December"]
print("Original list:")
print(months)
abbreviations=[month[:3] for month in months]
print('/'.join(abbreviation.upper() for abbreviation in abbreviations))
print("New List:")
print(abbreviations)

#Output=['January', 'February', 'March', 'April', 'May', 'JuneJuly', 'August', 'September', 'Octuber', 'November', 'December']
#JAN/FEB/MAR/APR/MAY/JUN/AUG/SEP/OCT/NOV/DEC
#New List:
#['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']