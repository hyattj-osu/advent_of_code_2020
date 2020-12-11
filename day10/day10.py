def chain_joltage_adapters(adapter_joltages):

    wall_joltage = 0
    built_in_adapter_joltage = max(adapter_joltages) + 3
    adapter_joltages.append(wall_joltage)
    adapter_joltages.append(built_in_adapter_joltage)

    sorted_adapters = sorted(adapter_joltages.copy())

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



def find_path_permutations(node_dict):

    reverse_node_list = list(node_dict.keys())
    reverse_node_list.reverse()

    permutation_dict = {}
    for node in reverse_node_list:
        permutations = 0

        if len(node_dict[node]["paths"]) == 0:
            permutations = 1
        else:
            for future_node in node_dict[node]["paths"]:
                permutations += permutation_dict[future_node]
        permutation_dict.update({node: permutations})
        
    print(f'Part 2: {permutation_dict[reverse_node_list[-1]]}')

    return()



def count_adapter_permutations(adapter_joltages):

    wall_joltage = 0
    built_in_adapter_joltage = max(adapter_joltages) + 3
    adapter_joltages.append(wall_joltage)
    adapter_joltages.append(built_in_adapter_joltage)

    sorted_adapters = sorted(adapter_joltages.copy())
    # rev_sorted_adapters.reverse()

    adapter_path_dict = {}
    for adapter in sorted_adapters:
        adapter_dict = {}
        potential_paths = []
        good_potential_paths = [adapter+1, adapter+2, adapter+3]
        for good_potential_path in good_potential_paths:
            if good_potential_path in sorted_adapters:
                potential_paths.append(good_potential_path)
        adapter_dict.update({"paths": potential_paths, "path_count": len(potential_paths)})
        # adapter_path_dict.udpate({adapter: adapter_dict}) # no idea why this throws an error?
        adapter_path_dict[adapter] = adapter_dict

    # for adapter in adapter_path_dict.keys():
    find_path_permutations(adapter_path_dict)

    return()



def main():

    # with open("./day10/example1.txt", 'r') as infile:
    # with open("./day10/example2.txt", 'r') as infile:
    with open("./day10/input.txt", 'r') as infile:
        lines = [int(line) for line in infile.readlines()]

    chain_joltage_adapters(lines)
    count_adapter_permutations(lines)

    return()



if __name__ == "__main__":
    main()