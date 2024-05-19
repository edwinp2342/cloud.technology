from shapes import Rectangle, Circle

# Using Rectangle
rect = Rectangle()
rect.display()
rect.setWidth(1.25)
rect.setHeight(1.25)
print(f"Get Width: {rect.getWidth()}")
print(f"Get Height: {rect.getHeight()}")
print(f"Area: {rect.area()}")

# Using Circle
circle = Circle(0)
circle.setRadius(10)
circle.display()
print(f"Get Radius: {circle.getRadius()}")
print(f"Area: {circle.area()}")
print(f"Circumference: {circle.circumference()}")
