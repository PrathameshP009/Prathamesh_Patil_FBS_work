angle1 = float(input("Enter first angle: "))
angle2 = float(input("Enter second angle: "))
angle3 = float(input("Enter third angle: "))

sum = angle1 + angle2 + angle3

if sum == 180 and angle1 > 0 and angle2 > 0 and angle3 > 0:
    print("The triangle is valid.")
else:
    print("The triangle is not valid.")
