# Define a function to read and display file contents using a loop
def read_file_with_loop(filename):
    try:
        with open(filename, 'r') as file:
            # Read each line in the file using a loop and print it
            for line in file:
                print(line.strip())  # strip() to remove newline characters
    except FileNotFoundError:
        print(f"The file {filename} was not found.")

# Define a function to read and display file contents using a list
def read_file_with_list(filename):
    try:
        with open(filename, 'r') as file:
            # Read all lines into a list and print each line
            lines = file.readlines()
            for line in lines:
                print(line.strip())  # strip() to remove newline characters
    except FileNotFoundError:
        print(f"The file {filename} was not found.")

# Example usage
# Assume 'Presidents.txt' is in the same directory as this script
filename = 'Presidents.txt'

print("Using Loop ------")
read_file_with_loop(filename)

print("\nUsing List ------")
read_file_with_list(filename)
