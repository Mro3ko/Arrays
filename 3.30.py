arr=[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
for i in range(0,len(arr)):
    for j in range (0,len(arr)):
        arr[i][j]=(i+1)*(j+1)
for row in arr:
    print(row)