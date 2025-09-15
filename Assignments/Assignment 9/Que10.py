num = int(input("Enter a number: "))
def reverse_number(n, rev=0):
    if n == 0:
        return rev
    return reverse_number(n // 10, rev * 10 + n % 10)

print("Reversed number:", reverse_number(num))
