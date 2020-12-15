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



def main():

    # with open("./day13/example.txt") as infile:
    with open("./day13/input.txt") as infile:
        lines = infile.read().splitlines()
        depart_start = int(lines[0])
        buses_in_service_raw = lines[1]

    best_bus = find_earliest_bus(depart_start, buses_in_service_raw)
    wait_time = best_bus['depart_time'] - depart_start

    print(f"Part 1: {wait_time * best_bus['bus_id']}")
    
    return()



if __name__ == "__main__":
    main()