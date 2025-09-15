#Star pyramid
rows = 5
for i in range(rows):
    print(" " * (rows - i - 1), end="")
    print("* " * (i + 1))
print()