arr=[[-38, 19], [5,40],[-7,11],[29,16]]
max_number=arr[0][0]
max_index=[0,0]
min_number=arr[0][0]
min_index=[0,0]
for i in range(0, len(arr)):
    for j in range(0,len(arr[i])):
        if arr[i][j]>max_number:
            max_number=arr[i][j]
            max_index=[i,j]
        elif arr[i][j]<min_number:
            min_number=arr[i][j]
            min_index=[i,j]
        else:
            continue
for row in arr:
    print(row)

print(f"max number: {max_number}, index: {max_index}")
print(f"min number: {min_number}, index: {min_index}")