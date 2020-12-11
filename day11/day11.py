from copy import deepcopy



"""
If a seat is empty (L) and there are no occupied seats adjacent to it, the seat becomes occupied.
If a seat is occupied (#) and four or more seats adjacent to it are also occupied, the seat becomes empty.
Otherwise, the seat's state does not change.
"""
def check_adjacent_seats_part1(row, col, seats):

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



def iterate_seats_part1(seats):

    next_seats = deepcopy(seats)

    for row, row_status in enumerate(seats):
        for col, seat_status in enumerate(row_status):
            if seat_status == 'L':   # empty
                occupied_adjacent_count = check_adjacent_seats_part1(row, col, seats)
                if occupied_adjacent_count == 0:
                    next_seats[row][col] = '#'
            elif seat_status == '#': # occupied
                occupied_adjacent_count = check_adjacent_seats_part1(row, col, seats)
                if occupied_adjacent_count >= 4:
                    next_seats[row][col] = 'L'

    seats = deepcopy(next_seats)
    return(seats)



def stabalize_seat_chaos_part1(seating_chart):

    seats_taken = 0
    previous_chart = deepcopy(seating_chart)
    current_chart = deepcopy(seating_chart)
    
    current_chart = iterate_seats_part1(previous_chart)
    while current_chart != previous_chart:
        previous_chart = deepcopy(current_chart)
        current_chart = iterate_seats_part1(previous_chart)

    seats_taken = sum([row.count('#') for row in current_chart])    
    
    return(seats_taken)



"""
As soon as people start to arrive, you realize your mistake. People don't just care about adjacent seats - they care about the first seat they can see in each of those eight directions!

Now, instead of considering just the eight immediately adjacent seats, consider the first seat in each of those eight directions.

Also, people seem to be more tolerant than you expected: it now takes five or more visible occupied seats for an occupied seat to become empty (rather than four or more from the previous rules).
"""
def check_visible_seats(row, col, seats, row_iter, col_iter):

    occupied_adjacent_count = 0

    check_row = row + row_iter
    check_col = col + col_iter
    while(check_col >= 0 and check_col < len(seats[row]) and check_row >= 0 and check_row < len(seats)):
        if seats[check_row][check_col] == '#':
            occupied_adjacent_count += 1
            break
        elif seats[check_row][check_col] == 'L':
            break
        check_col += col_iter
        check_row += row_iter

    return(occupied_adjacent_count)



def check_adjacent_seats_part2(row, col, seats):

    occupied_adjacent_count = 0

    for row_iter in range(-1, 2, 1):
        for col_iter in range(-1, 2, 1):
            if row_iter == 0 and col_iter == 0:
                continue # it is checking itself
            occupied_adjacent_count += check_visible_seats(row, col, seats, row_iter, col_iter)

    return(occupied_adjacent_count)



def iterate_seats_part2(seats):

    next_seats = deepcopy(seats)

    for row, row_status in enumerate(seats):
        for col, seat_status in enumerate(row_status):
            if seat_status == 'L':   # empty
                occupied_adjacent_count = check_adjacent_seats_part2(row, col, seats)
                if occupied_adjacent_count == 0:
                    next_seats[row][col] = '#'
            elif seat_status == '#': # occupied
                occupied_adjacent_count = check_adjacent_seats_part2(row, col, seats)
                if occupied_adjacent_count >= 5:
                    next_seats[row][col] = 'L'

    seats = deepcopy(next_seats)
    return(seats)



def stabalize_seat_chaos_part2(seating_chart):

    previous_chart = deepcopy(seating_chart)
    current_chart = deepcopy(seating_chart)
    
    current_chart = iterate_seats_part2(previous_chart)
    while current_chart != previous_chart:
        previous_chart = deepcopy(current_chart)
        current_chart = iterate_seats_part2(previous_chart)

    seats_taken = sum([row.count('#') for row in current_chart])    

    return(seats_taken)




def main():

    # with open("./day11/example.txt") as infile:
    with open("./day11/input.txt") as infile:
        lines = infile.read().splitlines()
        seats = [list(line) for line in lines]

    seats_taken = stabalize_seat_chaos_part1(seats)
    print(f'Part 1: {seats_taken}')

    seats_taken = stabalize_seat_chaos_part2(seats)
    print(f'Part 2: {seats_taken}')

    return()



if __name__ == "__main__":
    main()