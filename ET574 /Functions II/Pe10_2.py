def nameFormat(first, middle, last):
    """Prints the first name, middle initial, and last name in a title format."""
    # Ensure names are properly capitalized and middle name is reduced to initial with a period
    formatted_name = f"{first.title()} {middle[0].upper()}. {last.title()}"
    print(formatted_name)

def main():
    # Call nameFormat with positional arguments
    nameFormat('john', 'stu', 'smith')
    
    # Call nameFormat with keyword arguments
    nameFormat(first='john', middle='fitzgerald', last='kennedy')

# Call main() function to initiate the tasks to be performed
if __name__ == "__main__":
    main()
