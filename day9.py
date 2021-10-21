FILE = list(map(int, open("C:\\Users\\Alfonso\\Desktop\\Coding\\Advent of Code 2020\\Day9_Data.txt").read().splitlines()))
from itertools import combinations 

def part1(FILE):
    preamble_size = 25
    for index in range(preamble_size, len(FILE)):
        value = FILE[index]
        preamble = FILE[index - preamble_size: index]
        if not any(sum(x) == value for x in combinations(preamble,2)):
            return value

def part2(FILE):
    invalid_num = part1(FILE)
    for index in range(len(FILE)):
        for value in range(index):
            if sum(FILE[value:index]) == invalid_num:
                return min(FILE[value:index]) + max(FILE[value:index])

            
print(part1(FILE))
print(part2(FILE))