arr = [7,9,2,4,5,6]
arr_even=[]
arr_odd=[]
for i in arr:
    if i%2==0:
        arr_even.append(i)
    else:
        arr_odd.append(i)
        
print(arr)
print(arr_even)
print(arr_odd)
arr=arr_even+arr_odd
print(arr)