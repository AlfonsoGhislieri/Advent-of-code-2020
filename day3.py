FILE = open("C:/Users/Alfonso/Desktop/Coding/Advent of Code 2020/Day3_Data.txt").read().splitlines()

def tobogan(track, right_move, down_move):
    length_track, width_track = len(track), len(track[0])
    row, pos_in_row = 0, 0
    trees = 0
    while row < length_track:
        if track[row][pos_in_row] == "#":
            trees += 1
        row += down_move
        pos_in_row = (pos_in_row + right_move) % width_track
    return trees

print(tobogan(FILE, 3, 1)) # Part 1 
print(tobogan(FILE, 1, 1) * tobogan(FILE, 3, 1) * tobogan(FILE, 5, 1) * tobogan(FILE, 7, 1) * tobogan(FILE, 1, 2)) # Part 2