categories = ["Food", "Transport", "Rent","Entertainment"]
expenses = [500, 150, 1000, 200]

max_expense=expenses[0]
max_index=0

for i in range(1,len(expenses)):
    if expenses[i]>max_expense:
        max_expense=expenses[i]
        max_index=i

print(f"The most expensive category was{categories[max_index]}: {expenses[max_index]}$")