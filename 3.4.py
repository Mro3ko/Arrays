def maximum(arr):
    a=arr[0]
    for i in range(1,len(arr)-1):
        if arr[i]>a:
            a=arr[i]
    return a
def minimum(arr):
    a=arr[0]
    for i in range(1,len(arr)-1):
        if arr[i]<a:
            a=arr[i]
    return a


print(maximum( [-15, 8, -31, 47, -2, 19]))
print(minimum([ -15, 8, -31, 47, -2, 19]))
