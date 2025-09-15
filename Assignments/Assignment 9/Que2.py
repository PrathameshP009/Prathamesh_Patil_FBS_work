num = int(input("Enter a number: "))
def count_digits(n):
    return len(str(n))

def armstrong_sum(n, power):
    if n == 0:
        return 0
    digit = n % 10
    return (digit ** power) + armstrong_sum(n // 10, power)

def is_armstrong(n):
    return n == armstrong_sum(n, count_digits(n))

print(num, "is Armstrong" if is_armstrong(num) else "is not Armstrong")
