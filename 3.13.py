def occurs(number, array):
    for i in array:
        if i==number:
            return True
    return False

number=23
array=[15, 38, 7, 23, 14]
print(f"Number {number} appears in the array: {occurs(number, array)}")