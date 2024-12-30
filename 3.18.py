import MyArrays
array=[7,3,8,5,2]
arr_text=str(array[0])
for i in range(1,len(array)):
    arr_text+=", "+str(array[i])
print(f"Numbers: {arr_text}")
print(f"Second largest number: {MyArrays.second_largest(array)}")
print(f"Median: {MyArrays.median(array)}")
print(f"Smallest and largest number: {MyArrays.smallest_and_largest(array)}")
print(f"Numbers as a string: {MyArrays.array_string(array)}")
print(f"Difference between the largest and smallest values: {MyArrays.difference(array)}")

    
