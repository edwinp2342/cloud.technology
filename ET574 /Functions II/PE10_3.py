def nameFormat(first, last, middle=None):
    """Formats and prints the name depending on the presence of a middle name."""
    if middle:
        # If middle name is provided, format as: Last, First, M.
        formatted_name = f"{last.title()}, {first.title()}, {middle[0].upper()}."
    else:
        # If no middle name is provided, format as: Last, First
        formatted_name = f"{last.title()}, {first.title()}"
    return formatted_name

def main():
    # Call the function with keyword arguments for the name: james bond
    result1 = nameFormat(first='james', last='bond')
    
    # Call the function with keyword arguments for the name: henry indiana jones
    result2 = nameFormat(first='henry', middle='indiana', last='jones')
    
    # Print the results of the function calls
    print(result1)
    print(result2)

# Call main() function to initiate the tasks to be performed
if __name__ == "__main__":
    main()
