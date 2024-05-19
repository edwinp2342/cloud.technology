def createUser(**kwargs):
    """Creates and returns a dictionary from the given keyword arguments."""
    return kwargs

def printUser(user):
    """Prints the contents of the dictionary 'user'."""
    for key, value in user.items():
        print(f"{key}: {value}")

def main():
    # Create and print the user: John, age 43, job Programmer, Hobby Biking
    john = createUser(name="John", age=43, job="Programmer", hobby="Biking")
    printUser(john)
    print()  # Add a blank line for better readability between entries

    # Create and print the user: Sara, age 24, school QCC, major CSIS
    sara = createUser(name="Sara", age=24, school="QCC", major="CSIS")
    printUser(sara)

# Call main() function to initiate the tasks to be performed
if __name__ == "__main__":
    main()
