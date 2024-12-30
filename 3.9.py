def compare (arr1, arr2):
    if len(arr1)!=len(arr2):
        return False
    else:
        for i in range(len(arr1)):
            if arr1[i]==arr2[i]:
                continue
            else:
                return False
        return True

if compare(["water","book","sky"],["water","book","sky"]):
    print("Comparison: arrays are the same")
else:
    print("Comparison: arrays are not the same")

if compare([True,False], [True,False,True]):
    print("Comparison: arrays are the same")
else:
    print("Comparison: arrays are not the same")

if compare([5,3,1], [5,3,1]):
    print("Comparison: arrays are the same")
else:
    print("Comparison: arrays are not the same")

if compare([3,2,1],[3,2]):
    print("Comparison: arrays are the same")
else:
    print("Comparison: arrays are not the same")