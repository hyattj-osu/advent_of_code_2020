from copy import deepcopy



"""
If a seat is empty (L) and there are no occupied seats adjacent to it, the seat becomes occupied.
If a seat is occupied (#) and four or more seats adjacent to it are also occupied, the seat becomes empty.
Otherwise, the seat's state does not change.
"""
def check_adjacent_seats(row, col, seats):

    occupied_adjacent_count = 0

    for i in range(-1, 2, 1):
        for j in range(-1, 2, 1):
            check_row = row + i
            check_col = col + j

            if (0 > check_row) or (check_row >= len(seats)): # row out of bounds
                continue
            elif (0 > check_col) or (check_col >= len(seats[row])): # col out of bounds
                continue
            elif i == 0 and j == 0: # current seat
                continue
            if seats[check_row][check_col] == '#':
                occupied_adjacent_count += 1

    return(occupied_adjacent_count)



def iterate_seats(seats):

    next_seats = deepcopy(seats)

    for row, row_status in enumerate(seats):
        for col, seat_status in enumerate(row_status):
            if seat_status == 'L':   # empty
                occupied_adjacent_count = check_adjacent_seats(row, col, seats)
                if occupied_adjacent_count == 0:
                    next_seats[row][col] = '#'
            elif seat_status == '#': # occupied
                occupied_adjacent_count = check_adjacent_seats(row, col, seats)
                if occupied_adjacent_count >= 4:
                    next_seats[row][col] = 'L'

    seats = deepcopy(next_seats)
    return(seats)



def stabalize_seat_chaos(seating_chart):

    seats_taken = 0
    previous_chart = deepcopy(seating_chart)
    current_chart = deepcopy(seating_chart)
    
    current_chart = iterate_seats(previous_chart)
    while current_chart != previous_chart:
        previous_chart = deepcopy(current_chart)
        current_chart = iterate_seats(previous_chart)

    seats_taken = sum([row.count('#') for row in current_chart])    
    
    return(seats_taken)



def main():

    # with open("./day11/example.txt") as infile:
    with open("./day11/input.txt") as infile:
        lines = infile.read().splitlines()
        seats = [list(line) for line in lines]

    seats_taken = stabalize_seat_chaos(seats)
    print(f'Part 1: {seats_taken}')

    return()



if __name__ == "__main__":
    main()