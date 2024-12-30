numbers = [2, 3, 2, 5, 8, 1, 9, 8]
unique=[]
for i in numbers:
    liczba_wystapien=numbers.count(i)
    if liczba_wystapien>1:
        continue
    else:
        unique.append(i)
print(unique)
