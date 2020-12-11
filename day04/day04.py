import re

def part1():
    REQUIRED_FIELDS = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

    passports = []
    passport_index = 0
    passports.append({})
    # with open("./day04/example.txt", 'r') as infile:
    with open("./day04/input.txt", 'r') as infile:
        for line in infile:
            if not line.strip():
                passport_index += 1
                passports.append({})
                continue
            parameters = line.split()
            for parameter in parameters:
                param_key, param_value = parameter.split(':')
                passports[passport_index].update({param_key: param_value})

    valid_count = 0        
    for passport in passports:
        valid = True
        for field in REQUIRED_FIELDS:
            if field not in passport.keys():
                valid = False
                break
        if valid:
            valid_count += 1
    print(f'Part 1: {valid_count}')
    return()


"""
Part 2

byr (Birth Year) - four digits; at least 1920 and at most 2002.
iyr (Issue Year) - four digits; at least 2010 and at most 2020.
eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
hgt (Height) - a number followed by either cm or in:
If cm, the number must be at least 150 and at most 193.
If in, the number must be at least 59 and at most 76.
hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
pid (Passport ID) - a nine-digit number, including leading zeroes.
cid (Country ID) - ignored, missing or not.
"""
def part2():
    REQUIRED_FIELDS = {'byr': re.compile("^19[2-9][0-9]$|^200[0-2]$"), 
                       'iyr': re.compile("^20(1[0-9]|20)$"), 
                       'eyr': re.compile("^20(2[0-9]|30)$"), 
                       'hgt': re.compile("^(1([5-8][0-9]|9[0-3])cm|(59|6[0-9]|7[0-6])in)$"), 
                       'hcl': re.compile("^#[0-9a-f]{6}$"), 
                       'ecl': re.compile("^(amb|blu|brn|gry|grn|hzl|oth)$"), 
                       'pid': re.compile("^[0-9]{9}$")}

    passports = []
    passport_index = 0
    passports.append({})
    # with open("./day04/example.txt", 'r') as infile:
    with open("./day04/input.txt", 'r') as infile:
        for line in infile:
            if not line.strip():
                passport_index += 1
                passports.append({})
                continue
            parameters = line.split()
            for parameter in parameters:
                param_key, param_value = parameter.split(':')
                passports[passport_index].update({param_key: param_value})

    valid_count = 0        
    for passport in passports:
        valid = True
        for field in REQUIRED_FIELDS.keys():
            if field not in passport.keys() or not REQUIRED_FIELDS[field].match(passport[field]):
                valid = False
                break   
        if valid:
            valid_count += 1
    print(f'Part 2: {valid_count}')
    return()



def main():

    part1()
    part2()
    
    return()



if __name__ == "__main__":
    main()