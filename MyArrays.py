def second_largest(arr):
    if arr[1]>arr[0]:
        largest=arr[1]
        second_largest=arr[0]
    else:
        largest=arr[0]
        second_largest=arr[1]
    for i in range(2,len(arr)):
        if arr[i]>largest:
            second_largest=largest
            largest=arr[i]
        elif arr[i]>second_largest:
            second_largest=arr[i]
    return second_largest

def difference(arr):
    if arr[0]>arr[1]:
        largest=arr[0]
        smallest=arr[1]
    else:
        largest=arr[1]
        smallest=arr[0]
    for i in range(2,len(arr)):
        if arr[i]>largest:
            largest=arr[i]
        elif arr[i]<smallest:
            smallest=arr[i]
    return largest-smallest

def bubble_sort(arr):
    n=len(arr)

    for i in range(n):
        for j in range(n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1], arr[j]

    return arr

def median(arr):
    arr=bubble_sort(arr)
    if len(arr)%2==0:
        return (arr[len(arr)//2-1]+arr[(len(arr)//2)])/2
    elif len(arr)%2==1:
        return arr[len(arr)//2]
    
def smallest_and_largest(arr):
    if arr[0]>arr[1]:
        smallest=arr[1]
        largest=arr[0]
    else:
        smallest=arr[0]
        largest=arr[1]
    for i in range(2,len(arr)):
        if arr[i]>largest:
            largest=arr[i]
        elif arr[i]<smallest:
            smallest=arr[i]
    
    return str(smallest)+", "+str(largest)

def array_string(arr):
    result=str(arr[0])
    for i in range(1,len(arr)):
        result+="-"+str(arr[i])
    return result

if __name__=="__main__":
    print(second_largest([7,3,8,5,2]))