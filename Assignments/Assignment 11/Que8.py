#Print 1 to 100 in snakes and ladder pattern
for i in range(1, 101, 10):
    row = list(range(i, i + 10))
    if (i // 10) % 2 == 1:
        row.reverse()
    print(row)
