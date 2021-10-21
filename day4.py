FILE = open("C:/Users/Alfonso/Desktop/Coding/Advent of Code 2020/Day4_Data.txt").read().split("\n\n")

required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
valid_eyecolors = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
valid_haircolors = "0123456789abcdef"

def Part1(file):
    valid_passports = 0
    for passport in file:
        current_fields = 0
        passport_field = [field.split(":")[0] for field in passport.split()]
        for field in required_fields:
            if field in passport_field:
                current_fields += 1
        if current_fields >= 7 :
            valid_passports += 1
    return valid_passports

def Part2(file):
    valid_passports = 0
    for passport in file:
        passport_field = [field.split(":")[0] for field in passport.split()]
        passport_field_value = [field.split(":")[1] for field in passport.split()]
        passport_dictionary = dict(zip(passport_field,passport_field_value))
        if all(key in passport_dictionary for key in required_fields):  
            valid = True
            if not (1920 <= int(passport_dictionary["byr"]) <= 2002):
                valid = False
            if not (2010 <= int(passport_dictionary["iyr"]) <= 2020):
                valid = False
            if not (2020 <= int(passport_dictionary["eyr"]) <= 2030):
                valid = False
            if not ((passport_dictionary["hgt"][-2:] == "cm" and 150 <= int(passport_dictionary["hgt"][:-2]) <= 193) or (passport_dictionary["hgt"][-2:] == "in" and 59 <= int(passport_dictionary["hgt"][:-2]) <= 76)):
                valid = False
            if not(passport_dictionary["hcl"][0] == "#" and len(passport_dictionary["hcl"]) == 7 and(all(char in "0123456789abcdef" for char in passport_dictionary["hcl"][1:]))):
                    valid = False
            if not (passport_dictionary["ecl"] in valid_eyecolors):
                valid = False
            if not (len(passport_dictionary["pid"]) == 9 and all(char in '0123456789' for char in passport_dictionary["pid"])):
                    valid = False
            if valid:
                valid_passports += 1
    return valid_passports
    
print(Part1(FILE))
print(Part2(FILE))