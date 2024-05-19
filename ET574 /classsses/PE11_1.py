class Rectangle:
    # Initialize with default width and height as 1
    def __init__(self, width=1, height=1):
        self.width = width
        self.height = height
    
    # Display method to print the width and height
    def display(self):
        print(f"Width: {self.width}")
        print(f"Height: {self.height}")

# Creating two Rectangle objects
r1 = Rectangle(4, 5)
r2 = Rectangle()

# Displaying the attributes using the display method
r1.display()
r2.display()

# Printing the attributes directly
print(f"Width of r1 and r2: {r1.width} & {r2.width}")
print(f"Height of r1 and r2: {r1.height} & {r2.height}")
