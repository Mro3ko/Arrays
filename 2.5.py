cinema_seats = [
   ['A', 'A', 'B', 'A', 'A'],
   ['A', 'B', 'B', 'A', 'A'],
   ['A', 'A', 'A', 'A', 'B'],
   ['B', 'A', 'A', 'A', 'A'],
   ['A', 'B', 'A', 'A', 'A']
]
def seats_total(seats):
    total=0
    for row in seats:
        total+=len(row)
    return total

def seats_avaiable(seats):
    a=0
    for row in seats:
        for seat in row:
            if seat=="A":
                a+=1
    
    return a

def seats_booked(seats):
    b=0
    for row in seats:
        for seat in row:
            if seat=="B":
                b+=1
    return b

def seat_status(seat, row, place):
    if seat[row-1][place-1]=="A":
        return "Available"
    elif seat[row-1][place-1]=="B":
        return "Booked"

print('CINEMA INFORMATION TABLE')
print(f'Total seats:{seats_total(cinema_seats)}')
print(f'Seats available: {seats_avaiable(cinema_seats)}')
print(f'Seats booked:{seats_booked(cinema_seats)}')
print(f'Seat in row 1, place 1:{seat_status(cinema_seats, 1, 1)}')
print(f'Seat in row 5, place 5:{seat_status(cinema_seats, 5, 5)}')
print(f'Seat in row 3, place 5:{seat_status(cinema_seats, 3, 5)}')