
"""
From your starting position at the top-left, check the position that is right 3 and down 1. Then, check the position 
that is right 3 and down 1 from there, and so on until you go past the bottom of the map.

The same pattern repeats to the right many times

Starting at the top-left corner of your map and following a slope of right 3 and down 1, how many trees would you 
encounter?
"""
def part1(lines):
    num_trees = 0
    hor_index = 0
    width = len(lines[0])
    for index, line in enumerate(lines):
        if index == 0:  # skip counting the first line since we move down initially
            continue
        hor_index += 3
        if hor_index >= width:   # since the pattern repeats to the right, loop around
            hor_index -= width
        if line[hor_index] == '#':
            num_trees += 1
    print(f'Part 1: {num_trees}')
    return()



def check_trees(layout, hshift, vshift):
    num_trees = 0
    width = len(layout[0])
    height = len(layout)

    hor_index = 0
    ver_index = vshift

    while 0 <= ver_index < height:
        hor_index += hshift
        if hor_index >= width:
            hor_index -= width
        elif hor_index < 0:
            hor_index = width + hor_index

        if layout[ver_index][hor_index] == '#':
            num_trees += 1         

        ver_index += vshift

    return(num_trees)



"""
Determine the number of trees you would encounter if, for each of the following slopes, you start at the top-left corner 
and traverse the map all the way to the bottom:

Right 1, down 1.
Right 3, down 1. (This is the slope you already checked.)
Right 5, down 1.
Right 7, down 1.
Right 1, down 2.
"""
def part2(lines):
    list_trees = []
    list_trees.append(check_trees(lines, 1, 1))
    list_trees.append(check_trees(lines, 3, 1))
    list_trees.append(check_trees(lines, 5, 1))
    list_trees.append(check_trees(lines, 7, 1))
    list_trees.append(check_trees(lines, 1, 2))

    answer = 1
    for num_trees in list_trees:
        answer *= num_trees
    print(f'Part 2: {answer}')
    return()



def main():
    lines = []
    with open("./day03/input.txt", 'r') as infile:
        for line in infile:
            lines.append(line.rstrip('\n'))
    part1(lines)
    part2(lines)
    return()



if __name__ == "__main__":
    main()