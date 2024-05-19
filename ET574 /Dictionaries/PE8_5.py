rank = {1: "Freshman", 2: "Sophomore", 3: "Junior", 4: "Senior"}
user_input = 3 
output = ""
if user_input in rank:
    output = f"The rank is: {rank[user_input]}"
else:
    output = "Invalid number of years!"
output
