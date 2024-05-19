# 4a. Create a dictionary stuInfo with keys: name, gpa, and age
stuInfo = {'name': 'Edwin Pena', 'gpa': 4.0, 'age': 18}
# 4b. Use a loop and the items() method to print all keys and values
for key, value in stuInfo.items():
    print(f"{key}: {value}")
# 4c. Use the update() method to change the gpa to 4.0
stuInfo.update({'gpa': 4.0})
# 4d. Use a loop and the keys() method to print all keys and values
for key in stuInfo.keys():
    print(f"{key}: {stuInfo[key]}")
# 4e. Add a key 'major' with the value to the dictionary
stuInfo['major'] = 'Computer Science'
# 4f. Use a loop and the values() method to print all values
for value in stuInfo.values():
    print(value)
# 4g. Use two different ways to delete gpa and age in the dictionary
del stuInfo['gpa']  # First method using del
stuInfo.pop('age')  # Second method using pop
# 4h. Print the updated dictionary
print(stuInfo)
