FILE = open("C:/Users/Alfonso/Desktop/Coding/Advent of Code 2020/Day5_Data.txt").read().splitlines()

def part1(file):
    boarding_pass_list = []
    for boarding_pass in file:
        min_row, max_row = 0, 127
        min_col, max_col = 0, 7
        for char in boarding_pass:
            if char == "F": #Lower half 
                max_row = (min_row + max_row) // 2 
            elif char == "B": #Upper half
                min_row = (min_row + max_row) // 2 + 1 # +1 is added in order to round up 
            elif char == "L": #Lower half  
                max_col = (min_col + max_col) // 2
            elif char == "R": #Upper Half
                min_col = (min_col + max_col) // 2 + 1 # +1 is added in order to round up 
        boarding_pass_list.append(min_row * 8 + min_col)
    return (boarding_pass_list)     
 
def part2(file):
    boarding_pass_list = part1(file)
    min_seat_id, max_seat_id = min(boarding_pass_list), max(boarding_pass_list)
    for seat_id in range(min_seat_id, max_seat_id):
        if seat_id not in boarding_pass_list:
            return seat_id
        
print(max(part1(FILE)))
print(part2(FILE))