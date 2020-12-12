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

        adj_x = 0
        adj_y = 0
        adj_rot = 0

        if direction == 'N':
            adj_y = magnitude
        elif direction == 'E':
            adj_x = magnitude
        elif direction == 'S':
            adj_y = -magnitude
        elif direction == 'W':
            adj_x = -magnitude
        elif direction == 'F':
            adj_x = int(math.cos(math.radians(ship_rotation))) * magnitude
            adj_y = int(math.sin(math.radians(ship_rotation))) * magnitude
        elif direction == 'L':
            adj_rot = magnitude
        elif direction == 'R':
            adj_rot = -magnitude

        ship_x, ship_y, ship_rotation = adjust_ship(ship_x, ship_y, ship_rotation, adj_x, adj_y, adj_rot)

    return(ship_x, ship_y, ship_rotation)


"""
Action N means to move the waypoint north by the given value.
Action S means to move the waypoint south by the given value.
Action E means to move the waypoint east by the given value.
Action W means to move the waypoint west by the given value.
Action L means to rotate the waypoint around the ship left (counter-clockwise) the given number of degrees.
Action R means to rotate the waypoint around the ship right (clockwise) the given number of degrees.
Action F means to move forward to the waypoint a number of times equal to the given value.
The waypoint starts 10 units east and 1 unit north relative to the ship. The waypoint is relative to the ship; that is, 
if the ship moves, the waypoint moves with it.
"""
# https://stackoverflow.com/questions/34372480/rotate-point-about-another-point-in-degrees-python
def rotate_point(origin, point, angle):
    """
    Rotate a point counterclockwise by a given angle around a given origin.

    The angle should be given in degrees.
    """
    ox, oy = origin
    px, py = point

    qx = ox + math.cos(math.radians(angle)) * (px - ox) - math.sin(math.radians(angle)) * (py - oy)
    qy = oy + math.sin(math.radians(angle)) * (px - ox) + math.cos(math.radians(angle)) * (py - oy)
    return(qx, qy)



def follow_waypoints(instructions):

    ship_x = 0
    ship_y = 0
    ship_rotation = 0 # north=90deg, south=270deg or -90deg, etc
    wp_x = ship_x + 10
    wp_y = ship_y + 1

    for instruction in instructions:
        direction = instruction[0]
        magnitude = int(instruction[1:])

        if direction == 'N':
            wp_y += magnitude
        elif direction == 'E':
            wp_x += magnitude
        elif direction == 'S':
            wp_y -= magnitude
        elif direction == 'W':
            wp_x -= magnitude
        elif direction == 'F':
            for _ in range(magnitude):
                ship_x, ship_y, ship_rotation = adjust_ship(ship_x, ship_y, ship_rotation, wp_x, wp_y, 0)
        elif direction == 'L':
            wp_x, wp_y = rotate_point((0, 0), (wp_x, wp_y), magnitude)
        elif direction == 'R':
            wp_x, wp_y = rotate_point((0, 0), (wp_x, wp_y), -magnitude)

    return(ship_x, ship_y, ship_rotation)



def main():

    # with open("./day12/example.txt", 'r') as infile:
    with open("./day12/input.txt", 'r') as infile:
        lines = infile.read().splitlines()

    ship_x, ship_y, ship_rotation = follow_route(lines)
    manhattan_distance = abs(ship_x) + abs(ship_y)
    print(f'Part 1: {manhattan_distance}')

    ship_x, ship_y, ship_rotation = follow_waypoints(lines)
    manhattan_distance = int(abs(ship_x) + abs(ship_y))
    print(f'Part 2: {manhattan_distance}')
    return()



if __name__ == "__main__":
    main()