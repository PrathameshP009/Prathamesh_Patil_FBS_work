x = 65
for i in range(1, 6):
    print("  " * (5 - i), end="")
    for j in range(i * 2 - 1):
        print(chr(x + j), end=" ")
    print()