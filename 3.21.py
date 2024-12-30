def is_subset(arr1, arr2):
    for i in arr1:
        if not i in arr2:
            return False
        if arr1.count(i)>arr2.count(i):
            return False
    return True
print(is_subset([1,2,3,3], [2,3,6,4,6,4,2,0,2,1,1,3]))