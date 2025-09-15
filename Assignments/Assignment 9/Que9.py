m = int(input("Enter the base : "))
n = int(input("Enter the exponent : "))
def power(m, n):
    if n == 0:
        return 1
    return m * power(m, n - 1)

print("Power is :", power(m, n))
