import random
arr=[]
for i in range(0,3):
    row=[]
    for j in range(0,5):
        row.append(random.randint(1,10))
    arr.append(row)

for row in arr:
    print(row)

for i in range(0,3):
    arr[i][0],arr[i][4]=arr[i][4],arr[i][0]

print()

for row in arr:
    print(row)
