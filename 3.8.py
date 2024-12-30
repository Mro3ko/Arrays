def stars(n):
    result=""
    for i in range(0,n):
        result+="*"
    return result
        

arr=[2, 6, 4, 9, 7]
for i in arr:
    print(f"{i}: {stars(i)}")

    