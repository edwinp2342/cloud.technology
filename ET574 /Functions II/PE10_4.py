def printNames(*names):
    """Prints all contents of the names tuple."""
    for name in names:
        print(name, end=' ')
    print()  # For a newline after printing all names

def main():
    # Call the function printNames() with any number of name arguments
    printNames("Ann", "Bianca", "Coco", "Dora", "Emily")

# Call main() function to initiate the tasks to be performed
if __name__ == "__main__":
    main()
