import math

length = float(input("Enter length of rectangle: "))
breadth = float(input("Enter breadth of rectangle: "))
radius = float(input("Enter radius of semicircle: "))

area = (length * breadth) + (0.5 * math.pi * radius * radius)
perimeter = (2 * length) + (2 * breadth) + (math.pi * radius)

print("Area =", area)
print("Perimeter =", perimeter)
