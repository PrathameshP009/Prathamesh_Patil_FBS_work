import math

a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

D = b**2 - 4*a*c

if D > 0:
    root1 = (-b + math.sqrt(D)) / (2*a)
    root2 = (-b - math.sqrt(D)) / (2*a)
    print("\nThe roots are real and different.")
    print("Root 1 =", root1)
    print("Root 2 =", root2)
elif D == 0:
    root = -b / (2*a)
    print("\nThe roots are real and equal.")
    print("Root =", root)
else:
    real_part = -b / (2*a)
    imag_part = math.sqrt(-D) / (2*a)
    print("\nThe roots are complex and imaginary.")
    print("Root 1 =", real_part, "+", imag_part, "i")
    print("Root 2 =", real_part, "-",imag_part,"i")