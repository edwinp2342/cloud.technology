current_users = ['admin', 'tom', 'jerry', 'dora', 'george']
new_username = input("Enter your username: ")
normalized_current_users = [user.lower() for user in current_users]
if new_username.lower() in normalized_current_users:
    print(f"Sorry {new_username}, that name is taken.")
    print(f"Current users: {current_users}")
else:
    print(f"Great, {new_username} is still available.")
    current_users.append(new_username) 
    print(f"Updated users: {current_users}")
