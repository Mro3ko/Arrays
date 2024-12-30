import random
array=[]
for i in range(2):
    row=[]
    for j in range(4):
        row.append(random.randint(1,5))
    array.append(row)

for i in range (2):
    print(array[i])