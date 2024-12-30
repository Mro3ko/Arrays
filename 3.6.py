arr=[15, 8, 31, 47, 2, 19]
n=0
suma=0
while n<len(arr):
    suma+=arr[n]
    n+=1
print(round(suma/len(arr),2))