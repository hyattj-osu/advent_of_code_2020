def analyze_numbers_game(starting_numbers, end_number):
    
    numbers_dict = {}
    for index, starting_number in enumerate(starting_numbers):
        numbers_dict.update({starting_number: [index+1]})


    next_number_spoken = starting_numbers[-1]
    last_number_spoken = next_number_spoken
    for numbers_spoken in range(len(starting_numbers), end_number+1):
        last_number_spoken = next_number_spoken

        if len(numbers_dict[last_number_spoken]) == 1:
            next_number_spoken = 0
        else:
            next_number_spoken = numbers_dict[last_number_spoken][-1] - numbers_dict[last_number_spoken][-2]

        if next_number_spoken in numbers_dict.keys():
            numbers_dict[next_number_spoken].append(numbers_spoken+1)
        else:
            numbers_dict.update({next_number_spoken: [numbers_spoken+1]})

    print(f'Part 1: {last_number_spoken}')     
    
    return()



def main():

    # with open("./day15/example.txt", 'r') as infile:
    with open("./day15/input.txt", 'r') as infile:
        for line in infile:
            game_input = [int(x) for x in line.split(',')]
            analyze_numbers_game(game_input, 2020)

    return()



if __name__ == "__main__":
    main()