import math
length = float(input("Enter the length of rectangle;"))
breadth = float(input("Enter the breaadth of rectangle;"))
radius = float(input("Enter the radius of  circle;"))

rectangle_perimeter = 2 * (length + breadth)
rectangle_area = length * breadth

circle_perimeter = 2 * math.pi * radius
circle_area = math.pi * radius * radius

print("\n Rectangle ")
print(f"perimeter : {rectangle_perimeter}")
print(f"Area : {rectangle_area}")

print ("\n Circle ")
print(f"perimeter : {circle_perimeter}")
print(f"Area : {circle_area}")