FILE = open("C:/Users/Alfonso/Desktop/Coding/Advent of Code 2020/Day8_Data.txt").read().splitlines()

instructions = []
for line in FILE: #split the FILE into a list with each specific instruction as an entry
    instructions.append(line.split())

def part1(instructions):
    set_of_already_used_instructions = set()
    current_position, accumulator = 0 ,  0
    terminated = False
    while not terminated and current_position not in set_of_already_used_instructions:
        command, value = instructions[current_position][0] , int(instructions[current_position][1])
        set_of_already_used_instructions.add(current_position)
        if command == "jmp":
            current_position += value
        elif command == "nop":
            current_position += 1
        elif command == "acc":
            accumulator += value
            current_position += 1
        if current_position == len(instructions): #to check if current_position is the last line of code being run, used for solving Part2
            terminated = True
    return accumulator, terminated #returning terminated is required for the par2 code

def part2(instructions):
    for index in range(len(instructions)):
        instructions_copy = instructions.copy() #creating copy of list to modify with new potential replaced values
        if instructions[index][0] == "jmp":
            instructions_copy[index] = ("nop", instructions[index][1])
        if instructions[index][0] == "nop":
            instructions_copy[index] = ("jmp", instructions[index][1])
        accumulator, terminated = part1(instructions_copy)
        if terminated == True:
            break
    return accumulator

print(part1(instructions))
print(part2(instructions))