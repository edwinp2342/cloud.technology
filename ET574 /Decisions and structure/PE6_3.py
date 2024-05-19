usernames = ['ADMIN', 'Tom', 'Jerry', 'Bob', 'Dora']
if not usernames:
    print("We need to find some users.")
else:
    for username in usernames:
        if username == 'admin':
            print("Hello Admin, would you like to see a status report?")
        else:
            print(f"Hello {username}, thank you for logging in again!")
