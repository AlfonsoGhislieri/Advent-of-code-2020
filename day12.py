FILE = open("C:\\Users\\Alfonso\\Desktop\\Coding\\Advent of Code 2020\\Day12_Data.txt").read().splitlines()
DIRS = {"N": (0,1), "E": (1,0), "S": (0,-1), "W": (-1,0)}
ROTS = {0: (0,1), 90: (1,0), 180: (0,-1), 270: (-1,0)}

def part1(FILE):
    position = [0,0]
    facing = 90
    for instruction in FILE:
        direction = instruction[:1]
        value = int(instruction[1:])
        if direction == "F":
            x,y = ROTS[facing]
            position[0] += x * value
            position[1] += y * value
        elif direction in "RL": 
            if direction == "L":
                value= (0 - value)
            facing = (facing + value) % 360
        else:
            x,y = DIRS[direction]
            position[0] += x * value
            position[1] += y * value
    return abs(position[0]) + abs(position[1])

def rotate_waypoint(waypoint, value):
    waypoint_pos0 = waypoint[0]
    if value == 90:
        waypoint[0] = waypoint[1]
        waypoint[1] = 0 - waypoint_pos0
    if value == 180:
        waypoint[0] = 0 - waypoint[0]
        waypoint[1] = 0 - waypoint[1]
    if value == 270:
        waypoint[0] = 0 - waypoint[1]
        waypoint[1] = waypoint_pos0

def part2(FILE):
    position = [0,0]
    waypoint = [10,1]
    for instruction in FILE:
        direction = instruction[:1]
        value = int(instruction[1:])
        if direction == "F":
            x,y = waypoint
            position[0] += x * value
            position[1] += y * value
        elif direction in "RL":
            if direction == "L":
                value = (0 - value) % 360
            rotate_waypoint(waypoint, value)
        else:
            x,y = DIRS[direction]
            waypoint[0] += x * value
            waypoint[1] += y * value
    return abs(position[0]) + abs(position[1])
      

print(part1(FILE))
print(part2(FILE))