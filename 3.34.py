def identity_matrix(n):
    matrix=[]
    for i in range(0,n):
        row=[]
        for j in range(0,n):
            if i==j:
                row.append(1)
            else:
               row.append(0)
        matrix.append(row)
    return matrix

n=8
identity=identity_matrix(n)
for row in identity:
    print(row)