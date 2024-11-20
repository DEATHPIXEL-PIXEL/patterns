row = 3
col = 3
k = 1
for i in range (row):
    for j in range(col):
        if (i==0 or j==0 or j == col-1 or i==row-1 ):
        
             print (" 😂", end="")
        else: 
            print("   ", end="")
    print()