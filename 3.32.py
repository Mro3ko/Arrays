import random
array=[]
for i in range(3):
    row=[]
    for j in range(5):
        row.append(random.randint(1,10))
    array.append(row)
for wiersz in array:
    print(wiersz)

print()
array[0],array[2]=array[2], array[0]
 
for wiersz in array:
    print(wiersz)