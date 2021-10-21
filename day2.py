FILE = open("C:/Users/Alfonso/Desktop/Coding/Advent of Code 2020/Day2_Data.txt").read().splitlines()

def Part1(file):
    legal_passwords = 0
    for line in file:
        split1 = line.split("-")
        lower_value = int(split1[0])
        split2 = split1[1].split(" ")
        higher_value = int(split2[0])
        letter = split2[1].strip(":")
        password = split2[2]
        if lower_value <= password.count(letter) <= higher_value:
            legal_passwords += 1
    return legal_passwords

def Part2(file):
    legal_passwords = 0
    for line in file:
        split1 = line.split("-")
        first_number = int(split1[0])
        split2 = split1[1].split(" ")
        second_number = int(split2[0])
        letter = split2[1].strip(":")
        password = split2[2]
        if (password[first_number - 1] == letter) ^ (password[second_number - 1] == letter): # Using XOR, instead of and/or statements
            legal_passwords += 1
    return legal_passwords

print(Part1(FILE))
print(Part2(FILE))