import random
arr=[random.randint(1,20) for i in range (20)]
print(arr)
value=10
arr2=[i for i in arr if i>value ]
print(arr2)
print(len(arr2))