def function(arr2d):
    arr1d=[]
    for i in arr2d:
        for j in i:
            arr1d.append(j)

    return arr1d

arr1=[[2,3], [1,5]]
arr2=[[5,0,3,7,5],[9,0,9,1,2]]
arr3=[[2,1],[3,5],[7,4],[2,6]]
print(function(arr1))
print(function(arr2))
print(function(arr3))