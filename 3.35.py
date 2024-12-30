def transpose_matrix(m):
    m_transposed=[]
    for i in range(len(m[0])):
        new_row=[]
        for j in range(len(m)):
            new_row.append(m[j][i])
        m_transposed.append(new_row)
    
    return m_transposed

matrix=[[1,2,3,4,5],
        [6,7,8,9,0]]

matrix=transpose_matrix(matrix)
for row in matrix:
    print(row)



