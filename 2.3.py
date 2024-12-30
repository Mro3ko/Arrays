# [Food, Transport, Utilities]
monthly_expenses = [
   [200, 50, 100],  # Week 1
   [180, 60, 110],  # Week 2
   [220, 55, 105],  # Week 3
   [210, 65, 95]    # Week 4
]

food=0
for i in range(4):
    food+=monthly_expenses[i][0]

transport=0
for i in range(4):
    transport+=monthly_expenses[i][1]

utilities=0
for i in range(4):
    utilities+=monthly_expenses[i][2]

week1=0
for i in range(3):
    week1+=monthly_expenses[0][i]

week2=0
for i in range(3):
    week2+=monthly_expenses[1][i]

week3=0
for i in range(3):
    week3+=monthly_expenses[2][i]

week4=0
for i in range(3):
    week4+=monthly_expenses[3][i]
print('MONTHLY EXPENSES')
print('----------------')
print(f'Food:{food}')
print(f'Transport:{transport}')
print(f'Utilities:{utilities}')
print(f'Week 1: {week1}')
print(f'Week 2:{week2}')
print(f'Week 3:{week3}')
print(f'Week 4:{week4}')
print('---------------')
print(f'TOTAL:{food+transport+utilities}')