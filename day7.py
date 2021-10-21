FILE = open("C:/Users/Alfonso/Desktop/Coding/Advent of Code 2020/Day7_Data.txt").read().strip().splitlines()

import collections

def clean(line):
    return line.replace(' bags', '').replace(' bag', '').replace('.', '').strip()

def part1(FILE):
    rules = collections.defaultdict(list)
    for line in FILE:
        left_split, right_split = line.split(" contain ")[0],(line.split(" contain ")[1])
        holding_bag = clean(left_split)
        if clean(right_split) != "no other": #Skips rules when no extra bags are contained
            for rule in right_split.split(","):
                contained_bag = clean(rule[2:])
                rules[contained_bag].append(holding_bag) #Dictionary updated: what colour bags can be held by other bags
    return len(list_of_all_holders(rules,"shiny gold"))
   
def list_of_all_holders(dictionary, color):
    result = set(dictionary[color])
    for color in result:
        result = result.union(list_holders(dictionary,color))
    return result

def part2(FILE):
    rules = collections.defaultdict(list)
    for line in FILE:
        left_split, right_split = line.split(" contain ")[0],(line.split(" contain ")[1])
        holding_bag = clean(left_split)
        if clean(right_split) != "no other": #Skips rules when no extra bags are contained
            for rule in right_split.split(","):
                contained_bag = clean(rule)
                rules[holding_bag].append(contained_bag) #Dictionary updated: what colour bags can be held by other bags
    return (count_bag_contents(rules, "shiny gold"))

def count_bag_contents(dictionary, color):
    total = 0
    for bag in dictionary[color]:
        number_of_bags = int(bag[0])
        color = bag.split(maxsplit=1)[1]
        total += number_of_bags * (count_bag_contents(dictionary, color) + 1)
    return total
        


print(part1(FILE))   
print(part2(FILE))