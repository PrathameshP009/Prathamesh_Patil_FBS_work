for i in range (1,6):
    #column, i=row=left to right , j=column=up to down.
    for j in range(1,7-i):
        if(i==1 or j==1 or 6-i==j):#if we want to draw upward blank trangle pattern then i==j.
            print(j,end=" ")
        else:
            print(" ", end=" ")
    print()