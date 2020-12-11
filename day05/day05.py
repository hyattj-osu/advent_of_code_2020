"""
The first 7 characters will either be F or B; these specify exactly one of the 128 rows on the plane (numbered 0 
through 127). Each letter tells you which half of a region the given seat is in. Start with the whole list of rows; the 
first letter indicates whether the seat is in the front (0 through 63) or the back (64 through 127). The next letter 
indicates which half of that region the seat is in, and so on until you're left with exactly one row.

The last three characters will be either L or R; these specify exactly one of the 8 columns of seats on the plane 
(numbered 0 through 7). The same process as above proceeds again, this time with only three steps. L means to keep the 
lower half, while R means to keep the upper half.

Every seat also has a unique seat ID: multiply the row by 8, then add the column.
"""
def partition_binary(paths, val):
    lower_bound = 0
    upper_bound = val - 1
    for path in paths:
        if path == 'F' or path == 'L':
            upper_bound -= int((upper_bound - lower_bound) / 2) + 1
        elif path == 'B' or path == 'R':
            lower_bound += int((upper_bound - lower_bound) / 2) + 1
    loc = min([lower_bound, upper_bound])
    return(loc)



def parts(boarding_passes):
    NUM_ROWS = 128
    NUM_COLS = 8

    seats = {}
    for boarding_pass in boarding_passes:
        row_paths = boarding_pass[:7]
        col_paths = boarding_pass[7:]

        row = partition_binary(row_paths, NUM_ROWS)
        col = partition_binary(col_paths, NUM_COLS)

        seat_id = (row * 8) + col

        seat = {'row': row, 'col': col, 'seat_id': seat_id}
        seats.update({boarding_pass: seat})

    max_seat_id = max([seats[seat].get('seat_id') for seat in seats.keys()])   
    print(f'Part 1: {max_seat_id}')

    # seat_id_min = 0
    seat_id_max = ((NUM_ROWS-1) * 8) + (NUM_COLS-1)
    all_seats = [i for i in range(seat_id_max+1)]
    taken_seats = [seats[seat].get('seat_id') for seat in seats.keys()]
    open_seats = sorted(list(set(all_seats) - set(taken_seats)))
    
    # remove all empty seats at beginning and end
    for i, seat_id in enumerate(open_seats):
        if i == 0:
            continue
        prev_seat_id = open_seats[i-1]
        if (seat_id == prev_seat_id+1):  # seats are consecutively empty up to this seat_id
            continue
        usable_open_seat = seat_id
        break

    print(f'Part 2: {usable_open_seat}')
    return()
    


def main():

    lines = []
    # with open("./day05/example.txt", 'r') as infile:
    with open("./day05/input.txt", 'r') as infile:
        for line in infile:
            lines.append(line.strip())

    parts(lines)
    return()



if __name__ == "__main__":
    main()