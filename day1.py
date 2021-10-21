PUZZLE_INPUT = list(map(int, open("C:\\Users\\Alfonso\\Desktop\\Coding\\Advent of Code 2020\\Day1_Data.txt").read().split()))
def Part1(file):
    for index1 in range(len(PUZZLE_INPUT)):
        for index2 in range(index1):
            x = PUZZLE_INPUT[index1] 
            y = PUZZLE_INPUT[index2]
            if x + y == 2020:
                return(x*y)

def Part2(file):
    for index1 in range(len(PUZZLE_INPUT)):
        for index2 in range(index1):
            if PUZZLE_INPUT[index1] + PUZZLE_INPUT[index2] < 2020:
                for index3 in range(index2):
                    if (PUZZLE_INPUT[index1] + PUZZLE_INPUT[index2] + PUZZLE_INPUT[index3]) == 2020:
                        return PUZZLE_INPUT[index1] * PUZZLE_INPUT[index2] * PUZZLE_INPUT[index3]

print(Part1(PUZZLE_INPUT))  
print(Part2(PUZZLE_INPUT))