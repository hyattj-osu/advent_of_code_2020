import re
from itertools import combinations



def execute_commands_bitmask(commands):

    docking_dict = {}    
    for command in commands:
        if "mask" in command:
            bitmask_string = command.split("=")[1].strip()
        elif "mem" in command:
            address = int(re.match(r"mem\[([0-9]*)\]", command).group(1))
            value_int = int(command.split("=")[1].strip())
            value_bin = f'{value_int:b}'.zfill(36)

            masked_bin = ''
            for bit, value in enumerate(bitmask_string):
                if value == 'X':
                    masked_bin += value_bin[bit]
                else:
                    masked_bin += value

            docking_dict.update({address: int(masked_bin, 2)})

    sum_addresses = sum(docking_dict.values())
    print(f'Part 1: {sum_addresses}')

    return()



def execute_commands_decoder(commands):

    docking_dict = {}    
    for command in commands:
        if "mask" in command:
            bitmask_string = command.split("=")[1].strip()
        elif "mem" in command:
            address_int = int(re.match(r"mem\[([0-9]*)\]", command).group(1))
            address_bin = f'{address_int:b}'.zfill(36)
            value_int = int(command.split("=")[1].strip())

            masked_bin = ''
            for bit, value in enumerate(bitmask_string):
                if value == '0':
                    masked_bin += address_bin[bit]
                elif value == '1':
                    masked_bin += value
                else:
                    masked_bin += 'X'

            all_addresses = []
            num_floating_bits = masked_bin.count('X')
            for i in range(2 ** num_floating_bits):
                cur_address = masked_bin
                permutation = f'{i:b}'.zfill(num_floating_bits)
                for bit in permutation:
                    cur_address = cur_address.replace('X', bit, 1)
                all_addresses.append(cur_address)

            for address in all_addresses:
                docking_dict.update({address: value_int})

    sum_addresses = sum(docking_dict.values())
    print(f'Part 2: {sum_addresses}')

    return()



def main():

    # with open("./day14/example1.txt") as infile:
    # with open("./day14/example2.txt") as infile:
    with open("./day14/input.txt") as infile:    
        lines = infile.read().splitlines()

    execute_commands_bitmask(lines)
    execute_commands_decoder(lines)

    return()



if __name__ == "__main__":
    main()