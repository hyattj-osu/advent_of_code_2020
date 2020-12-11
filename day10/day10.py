def chain_joltage_adapters(adapter_joltages):

    wall_joltage = 0
    built_in_adapter_joltage = max(adapter_joltages) + 3
    adapter_joltages.append(wall_joltage)
    adapter_joltages.append(built_in_adapter_joltage)

    sorted_adapters = sorted(adapter_joltages.copy())

    if len(sorted_adapters) < 2:
        return()

    joltage_diff_1_count = 0
    joltage_diff_3_count = 0
    for i in range(1, len(sorted_adapters)):
        joltage_diff = sorted_adapters[i] - sorted_adapters[i-1]
        if joltage_diff == 1:
            joltage_diff_1_count += 1
        elif joltage_diff == 3:
            joltage_diff_3_count += 1

    # print(f'D1: {joltage_diff_1_count}, D3: {joltage_diff_3_count}')
    print(f'Part 1: {joltage_diff_1_count * joltage_diff_3_count}')

    return()



def main():

    # with open("./day10/example1.txt", 'r') as infile:
    # with open("./day10/example2.txt", 'r') as infile:
    with open("./day10/input.txt", 'r') as infile:
        lines = [int(line) for line in infile.readlines()]

    chain_joltage_adapters(lines)

    return()



if __name__ == "__main__":
    main()