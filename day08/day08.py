def check_accumulator_at_repeat_or_end(instructions):

    return_dict = {}
    return_dict.update({'code': 0})

    program_over = False
    repeat_instruction = False
    line_indeces_executed = []
    current_index_number = 0
    last_line_index = len(instructions) - 1
    accumulator = 0
    while not program_over and not repeat_instruction:
        
        line_indeces_executed.append(current_index_number)

        command, value = instructions[current_index_number].split()
        value = int(value)

        if command == "nop":
            # do nothing; execute next line
            current_index_number += 1
        elif command == "acc":
            # increase the accumulator and execute next line
            accumulator += value
            current_index_number += 1
        elif command == "jmp":
            # move the index where the jump dictates
            current_index_number += value

        if current_index_number > last_line_index:
            program_over = True
        if current_index_number in line_indeces_executed:
            repeat_instruction = True


    if repeat_instruction:
        return_dict.update({'code': 1})

    return_dict.update({'accumulator': accumulator})
    return(return_dict)



# attempts to fix boot code by either changing one nop->jmp or one jmp->nop
def fix_instructions(instructions):

    new_instructions = []
    new_instructions = instructions.copy()

    for index, instruction in enumerate(instructions):
        command = instruction.split()[0]

        if command == "nop":
            new_instructions[index] = instructions[index].replace("nop", "jmp")
        elif command == "jmp":
            new_instructions[index] = instructions[index].replace("jmp", "nop")

        new_results = check_accumulator_at_repeat_or_end(new_instructions)
        if new_results['code'] == 1:    # repeat detected
            new_instructions = instructions.copy()
        elif new_results['code'] == 0:  # no repeat; code finished normally
            return(new_results)

    return({'code': 1, 'accumulator': 0})



def main():

    # with open("./day08/example.txt", 'r') as infile:
    with open("./day08/input.txt", 'r') as infile:
        instructions = infile.read().splitlines()

    # Part 1
    part1_dict = check_accumulator_at_repeat_or_end(instructions)
    print(f"Part 1: {part1_dict['accumulator']}")

    # Part 2
    part2_dict = fix_instructions(instructions)
    if part2_dict['code'] == 0:
        print(f"Part 2: {part2_dict['accumulator']}")

    return()



if __name__ == "__main__":
    main()