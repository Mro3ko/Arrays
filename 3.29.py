def create_2d_arr(x,y):
    array=[]
    for i in range(x):
        row=[]
        for j in range(y):
            row.append(0)
        array.append(row)
    return array

matrix=create_2d_arr(8,5)
for row in matrix:
    print(row)


            