FILE = open("C:\\Users\\Alfonso\\Desktop\\Coding\\Advent of Code 2020\\Day11_Data.txt").read().splitlines()

def part1():
    original_layout = {}
    for x, row in enumerate(FILE):
        for y, seat in enumerate(row):
            original_layout[x,y] = seat
    
    layout = {}
    while True:
        for (x,y),seat in original_layout.items():
            if seat == ".":
                layout[x,y] = "."
            elif seat == "L":
                adjacent = ""
                for i in range(-1,2):
                    for j in range(-1,2):
                        if i == 0 and j == 0: #ignores seat in question 
                            continue
                        adjacent += original_layout.get((x + i , y + j),".")
                occupied = adjacent.count("#")
                
                if not occupied:
                    layout[x,y] = "#"
            
            elif seat == "#":
                adjacent = ""
                for i in range(-1,2):
                    for j in range(-1,2):
                        if i == 0 and j == 0: #ignores seat in question 
                            continue
                        adjacent += original_layout.get((x + i , y + j),".")
                occupied = adjacent.count("#")
                
                if occupied >= 4:
                    layout[x,y] = "L"
        
        if layout == original_layout:
            break
        original_layout = {key: value for key, value in layout.items()}
    
    result = 0
    for elem in layout.values():
        if elem == "#":
            result += 1
    return result


def part2():
    original_layout = {}
    for x, row in enumerate(FILE):
        for y, seat in enumerate(row):
            original_layout[x,y] = seat
    
    def check_occupied(r,c, direction):
        while True:
            r = r + direction[0]
            c = c + direction[1]
            try:
                if original_layout[r,c] == "#":
                    return 1
                if original_layout[r,c] == "L":
                    return 0
            except KeyError: 
                return 0
    
    layout = {}   
    while True:
        for (x,y),seat in original_layout.items():
            if seat == ".":
                layout[x,y] = "."
            elif seat == "L":
                occupied = 0
                for i in range(-1,2):
                    for j in range(-1,2):
                        if i == 0 and j == 0: #ignores seat in question 
                            continue
                        occupied += check_occupied(x, y,(i,j))
                
                if not occupied:
                    layout[x,y] = "#"
            
            elif seat == "#":
                occupied = 0
                for i in range(-1,2):
                    for j in range(-1,2):
                        if i == 0 and j == 0: #ignores seat in question 
                            continue
                        occupied += check_occupied(x, y,(i,j))
                
                if occupied >= 5:
                    layout[x,y] = "L"
        
        if layout == original_layout:
            break
        original_layout = {key: value for key, value in layout.items()}
    
    result = 0
    for elem in layout.values():
        if elem == "#":
            result += 1
    return result

print(part1())
print(part2())