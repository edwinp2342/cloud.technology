def printList(p):
    """Prints all values in the list p."""
    for item in p:
        print(item, end=' ')

def main():
    # Create a list of strings
    lst = ["apple", "banana", "cherry"]
    # Call the function printList() with lst as an argument
    printList(lst)

# Call main() function to initiate the tasks to be performed
if __name__ == "__main__":
    main()
