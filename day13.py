FILE = open("C:\\Users\\Alfonso\\Desktop\\Coding\\Advent of Code 2020\\Day13_Data.txt").read().split("\n")

def part1():
    current_time = int(FILE[0])
    busses = set(FILE[1].split(","))
    busses.remove("x")
    bus_dict = {bus: (int(bus) - current_time % int(bus)) for bus in busses}
    first_bus = min(bus_dict, key = bus_dict.get)
    time_to_wait = bus_dict[first_bus]
    return (int(first_bus) * time_to_wait)