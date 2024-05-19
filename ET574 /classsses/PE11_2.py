from rectangle import Rectangle

# Instantiate two objects, one with arguments and one without
r1 = Rectangle(4, 5)
r2 = Rectangle()

# Display initial state
r1.display()
r2.display()

# Print initial areas
print(f"Area: {r1.area()}")
print(f"Area: {r2.area()}")

# Update r2 dimensions and display updated measurements
r2.setWidth(6)
r2.setHeight(6)
r2.display()

# Get and print updated measurements and area
print(f"Get Width: {r2.getWidth()}")
print(f"Get Height: {r2.getHeight()}")
print(f"Area: {r2.area()}")
