class Circle:
    def __init__(self, radii):
        self.radii = radii
        self.__pi = 3.141

    def area(self, radius):
        return self.__pi * (radius ** 2)

    def perimeter(self, radius):
        return 2 * self.__pi * radius

# Create instance with the given list
circle = Circle([10, 501, 22, 37, 100, 999, 87, 351])

# Calculate Area and Perimeter for each radius in the list
for radius in circle.radii:
    print(f"Radius: {radius}, Area: {circle.area(radius)}, Perimeter: {circle.perimeter(radius)}")
