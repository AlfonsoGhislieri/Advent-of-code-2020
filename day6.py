FILE = open("C:/Users/Alfonso/Desktop/Coding/Advent of Code 2020/Day6_Data.txt").read().strip().split("\n\n")

def part1(groups):
    sum_of_yes = 0
    for group in groups:
        sum_of_yes += (len(set(group.replace("\n", ""))))
    return sum_of_yes
        
def part2(groups):
    sum_of_yes = 0
    for group in groups:
        group_dictionary = {}
        for char in group:
            if char not in group_dictionary:
                group_dictionary[char] = 0
            group_dictionary[char] += 1
        group_size = len(group.split('\n'))
        for value in group_dictionary.values():
            if value == group_size:
                sum_of_yes += 1
    return sum_of_yes
        
print(part1(FILE))
print(part2(FILE))