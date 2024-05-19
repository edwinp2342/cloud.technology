import random

def average(*grades):
    """Calculates and returns the average of all provided grades."""
    if grades:  # Check if grades tuple is not empty
        return sum(grades) / len(grades)
    else:
        return 0  # Return 0 if no grades are provided to avoid division by zero

def main():
    # Call the average function with specific arguments
    avg1 = average(95, 87, 83, 74)
    print(f"Average of 95, 87, 83, 74: {avg1:.2f}")

    # Create two random integers, x and y
    x = random.randint(-100, 0)
    y = random.randint(0, 100)

    # Call the average function with x and y
    avg2 = average(x, y)
    print(f"Average of two random numbers, {x}, {y}: {avg2:.2f}")

# Call main() function to initiate the tasks to be performed
if __name__ == "__main__":
    main()
