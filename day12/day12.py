import math



"""
Action N means to move north by the given value.
Action S means to move south by the given value.
Action E means to move east by the given value.
Action W means to move west by the given value.
Action L means to turn left the given number of degrees.
Action R means to turn right the given number of degrees.
Action F means to move forward by the given value in the direction the ship is currently facing.
The ship starts by facing east.
"""
def adjust_ship(loc_x, loc_y, loc_rot, adj_x, adj_y, adj_rot):

    new_x = loc_x + adj_x
    new_y = loc_y + adj_y
    new_rot = (loc_rot + adj_rot) % 360

    return(new_x, new_y, new_rot)



def follow_route(instructions):

    ship_x = 0
    ship_y = 0
    ship_rotation = 0 # north=90deg, south=270deg or -90deg, etc

    for instruction in instructions:
        direction = instruction[0]
        magnitude = int(instruction[1:])

        if direction == 'N':
            ship_x, ship_y, ship_rotation = adjust_ship(ship_x, ship_y, ship_rotation, 0, magnitude, 0)
        elif direction == 'E':
            ship_x, ship_y, ship_rotation = adjust_ship(ship_x, ship_y, ship_rotation, magnitude, 0, 0)
        elif direction == 'S':
            ship_x, ship_y, ship_rotation = adjust_ship(ship_x, ship_y, ship_rotation, 0, -magnitude, 0)
        elif direction == 'W':
            ship_x, ship_y, ship_rotation = adjust_ship(ship_x, ship_y, ship_rotation, -magnitude, 0, 0)
        elif direction == 'F':
            adj_x = int(math.cos(math.radians(ship_rotation))) * magnitude
            adj_y = int(math.sin(math.radians(ship_rotation))) * magnitude
            ship_x, ship_y, ship_rotation = adjust_ship(ship_x, ship_y, ship_rotation, adj_x, adj_y, 0)
        elif direction == 'L':
            ship_x, ship_y, ship_rotation = adjust_ship(ship_x, ship_y, ship_rotation, 0, 0, magnitude)
        elif direction == 'R':
            ship_x, ship_y, ship_rotation = adjust_ship(ship_x, ship_y, ship_rotation, 0, 0, -magnitude)

    return(ship_x, ship_y, ship_rotation)



def main():

    # with open("./day12/example.txt", 'r') as infile:
    with open("./day12/input.txt", 'r') as infile:
        lines = infile.read().splitlines()

    ship_x, ship_y, ship_rotation = follow_route(lines)
    manhattan_distance = abs(ship_x) + abs(ship_y)
    print(f'Part 1: {manhattan_distance}')

    return()



if __name__ == "__main__":
    main()