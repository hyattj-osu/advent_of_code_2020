def find_non_pattern_value(nums, back_trace_length):

    if len(nums) < back_trace_length:
        return()

    for base_index in range(back_trace_length, len(nums)):
        equal_to_sum = False
        for n1 in range(base_index-back_trace_length, base_index):
            for n2 in range(n1+1, base_index):
                sum = nums[n1] + nums[n2]
                if sum == nums[base_index]:
                    equal_to_sum = True
        if not equal_to_sum:
            print(f'Part 1: {nums[base_index]}') 
            return(nums[base_index])                
            
    return()


def find_contiguous_sum(nums, desired_sum):

    for i, num in enumerate(nums):
        running_sum = 0
        min_val = num
        max_val = num
        for j in range(i, len(nums)):
            running_sum += nums[j]
            min_val = min(min_val, nums[j])
            max_val = max(max_val, nums[j])
            if running_sum > desired_sum:
                break
            if running_sum == desired_sum:
                calc = min_val + max_val
                print(f'Part 2: {calc}')
                return()   

    return()



def main():

    # with open("./day09/example.txt", 'r') as infile:
    with open("./day09/input.txt", 'r') as infile:
        lines = [int(line) for line in infile.readlines()]

    # value = find_non_pattern_value(lines, 5) # example.txt
    value = find_non_pattern_value(lines, 25) # input.txt

    find_contiguous_sum(lines, value)

    return()



if __name__ == "__main__":
    main()