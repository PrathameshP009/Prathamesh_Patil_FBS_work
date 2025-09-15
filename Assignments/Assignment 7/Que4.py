n = 5
for i in range(1, n + 1):
    print("  "*(n - i), end="")  # Print leading spaces
    for j in range(i, i * 2):
        print(j, end=" ")
    for j in range(i * 2 - 2, i - 1, -1): 
        print(j, end=" ")
    print()
