arr=[15, 8, 31, 47, 2, 19]
reversed_list = []

'''for i in range(len(arr)-1,-1,-1):
    reversed_list.append(arr[i])
print(reversed_list)'''

i=len(arr)-1
while i >=0:
    reversed_list.append(arr[i])
    i-=1
print(arr)
print(reversed_list)