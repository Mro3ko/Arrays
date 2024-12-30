import random

def rand_element(array):
    n=random.randint(0,len(array)-1)
    return array[n]

arr=[7,9,2,4,5,6]
print(rand_element(arr))