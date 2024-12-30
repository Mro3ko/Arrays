def no_of_occurrences(tuple, value):
    counter=0
    for element in tuple:
        if element==value:
            counter+=1
    return counter

tuple=(50,20,40,50,30,50)
value=50
print(no_of_occurrences(tuple, value))