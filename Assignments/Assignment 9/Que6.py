def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

# Print first n terms
terms = int(input("Enter number of terms: "))
for i in range(terms):
    print(fibonacci(i), end=" ")
