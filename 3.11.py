def bubblesort(array):
    for i in range(0,len(array)):
        for j in range(0,len(array)-1-i):
            if array[j]>array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array

print(bubblesort([2, 3, 2, 5, 8, 1, 9, 8]))