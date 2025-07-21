rows = 5
cols = 5

for i in range(rows):
    
    for j in range(cols):
        if (i + j) % 2 == 0:
            print("1", end="")
        else:
            print("0", end= "")
        
    print(" ")
print()