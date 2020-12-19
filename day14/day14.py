import re



def execute_commands(commands):

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



def main():

    # with open("./day14/example.txt") as infile:
    with open("./day14/input.txt") as infile:    
        lines = infile.read().splitlines()

    execute_commands(lines)

    return()



if __name__ == "__main__":
    main()