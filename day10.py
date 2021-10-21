from collections import defaultdict

FILE = list(map(int, open("C:\\Users\\Alfonso\\Desktop\\Coding\\Advent of Code 2020\\Day10_Data.txt").read().splitlines()))
FILE.sort() #sorting list in ascending order
FILE.append(FILE[-1] + 3) #adding device's built-in adapter at end of the list
FILE.insert(0,0) #adding charging effective joltage rating value(0) at start of the list

def part1(FILE):
    jolt1, jolt3 = 0, 0
    for x,y in zip(FILE,FILE[1:]):
        if x + 1 == y:
            jolt1 += 1
        elif x + 3 == y:
            jolt3 += 1
    return (jolt1 * jolt3)

memory = {}
# Using Dynamic programming: the number of ways to complete the adapter chain given the position you are cucrently at FILE[x]
def part2(x):
    if x == len(FILE)-1: # Ending the recursive loop when only 1 way to get to end of chain
        return 1
    if x in memory:
        return memory[x]
    count = 0
    for y in range(x+1,len(FILE)):
        if FILE[y] - FILE[x]<=3:
            count += part2(y)
    memory[x] = count
    return count
    
print(part1(FILE))
print(part2(0))