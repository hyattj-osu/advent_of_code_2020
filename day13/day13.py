import numpy as np
from functools import reduce



def find_earliest_bus(depart_start, buses_in_service_raw):

    buses_in_service = [bus_id for bus_id in buses_in_service_raw.split(',') if bus_id != 'x']

    best_bus = {}
    for i, bus_id in enumerate(buses_in_service):
        if bus_id == 'x':
            continue

        earliest_bus_depart_time = int(bus_id)
        while earliest_bus_depart_time < depart_start:
            earliest_bus_depart_time += int(bus_id)

        if (i == 0) or (earliest_bus_depart_time < best_bus['depart_time']):
            best_bus.update({'bus_id': int(bus_id), 'depart_time': earliest_bus_depart_time})

    return(best_bus)


"""
The idea is to solve a system of equations
For the example 7,13,x,x,59,x,31,19,

 7*x_0 = t
13*x_1 = t + 1
59*x_2 = t + 4
31*x_3 = t + 6
19*x_4 = t + 7

For each integer 't', we can solve the equations. If all answers are whole numbers, than we have our final solution.

This solution works, but takes forever.
"""
def find_bus_offsets(bus_rules):

    right_side = []
    left_side = []
    for n, rule in enumerate(bus_rules.split(',')):
        if rule == 'x':
            continue
        left_side.append(int(rule))
        right_side.append(n)
    
    """
    From the example, the below produces:
    [[7,  0,  0,  0,  0], 
     [0, 13,  0,  0,  0], 
     [0,  0, 59,  0,  0], 
     [0,  0,  0, 31,  0], 
     [0,  0,  0,  0, 19]]
    """
    arrays = []
    for i in range(len(left_side)):
        arrays.append([])
        if i != 0:
            arrays[i] = [0] * i # pad the front with zeroes
        arrays[i].append(int(left_side[i]))
        arrays[i].extend([0] * (len(left_side)-1-i)) # pad the back with zeroes

    a = np.array(arrays, dtype=np.float)

    t = 1
    all_ints = False
    while not all_ints:
        b = np.array([t + x for x in right_side])

        ans = np.linalg.solve(a, b)
        all_ints = all([x.is_integer() for x in ans])

        t += 1

    return(t)



"""
Part 2 can be solved instead using the Chinese Remainder Theorem instead of brute-forcing for 80 years
Thanks trthomas for pointing this out.
Code from: https://rosettacode.org/wiki/Chinese_remainder_theorem#Python_3.6

Effectively, instead of the system of equations of above, we want the following:

t ≡ 0(mod  7)
t ≡ 1(mod 13)
t ≡ 4(mod 59)
t ≡ 6(mod 31)
t ≡ 7(mod 19)

or -> x ≡ a_k (mod n_k)

Our 'n' values will be the bus ID and our 'a' will be the timestep difference.
We make a matrix out of the 'a' and 'n' lists.
n = [7, 13, 59, 31, 19]; a = [0, 1, 4, 6, 7]

chinese_remainder(n, a) gives a unique solution to this problem, but not the minimum, which is what we want

"""
def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a*b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod
 
 
 
def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a%b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1



def find_bus_offsets_via_cnt(buses_in_service_raw):

    a = []
    n = []
    for i, bus_id in enumerate(buses_in_service_raw.split(',')):
        if bus_id == 'x':
            continue
        n.append(int(bus_id))
        a.append(i)

    return(n, a)



def main():

    # with open("./day13/example.txt") as infile:
    with open("./day13/input.txt") as infile:
        lines = infile.read().splitlines()
        depart_start = int(lines[0])
        buses_in_service_raw = lines[1]

    best_bus = find_earliest_bus(depart_start, buses_in_service_raw)
    wait_time = best_bus['depart_time'] - depart_start
    print(f"Part 1: {wait_time * best_bus['bus_id']}")

    # find_bus_offsets(buses_in_service_raw)

    # examples = ["17,x,13,19", "67,7,59,61", "67,x,7,59,61", "67,7,x,59,61", "1789,37,47,1889"]
    # for example in examples:
    #     n, a = find_bus_offsets_via_cnt(example)
    #     uniq_solution = chinese_remainder(n, a)
    #     N = 1
    #     for val in n:
    #         N *= val
    #     min_timestep = N - uniq_solution
    #     print(f"Part 2: {min_timestep}")

    n, a = find_bus_offsets_via_cnt(buses_in_service_raw)
    uniq_solution = chinese_remainder(n, a)

    N = 1
    for val in n:
        N *= val

    min_timestep = N - uniq_solution
    print(f"Part 2: {min_timestep}")
    
    return()



if __name__ == "__main__":
    main()