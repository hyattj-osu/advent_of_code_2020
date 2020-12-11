# Part 1: How many passwords are valid according to their policies?
# Part 2: How many passwords are valid according to the new interpretation of the policies?


# part 1
def find_valid_passwords_1(lines):
    num_valid_passwords = 0
    for line in lines:
        num_range = line.split()[0]
        desired_char = line.split()[1].split(':')[0]
        password = line.split()[2]

        low_bound = int(num_range.split('-')[0])
        high_bound = int(num_range.split('-')[1])

        char_count = password.count(desired_char)
        if low_bound <= char_count <= high_bound:
            num_valid_passwords += 1

    print(f'Part 1 valid passwords: {num_valid_passwords}')

    return()


# part 2
def find_valid_passwords_2(lines):
    num_valid_passwords = 0
    for line in lines:
        index_locations = line.split()[0]
        desired_char = line.split()[1].split(':')[0]
        password = line.split()[2]

        index1 = int(index_locations.split('-')[0]) - 1
        index2 = int(index_locations.split('-')[1]) - 1

        # need an XOR of the two indices
        index1_match = password[index1] == desired_char
        index2_match = password[index2] == desired_char
        if index1_match ^ index2_match:
            num_valid_passwords += 1

    print(f'Part 2 valid passwords: {num_valid_passwords}')

    return()



def main():
    lines = []
    with open("./day02/input.txt", 'r') as infile:
        for line in infile:
            lines.append(line.rstrip('\n'))
    # find_valid_passwords_1(lines)
    find_valid_passwords_2(lines)

    return()



if __name__ == "__main__":
    main()