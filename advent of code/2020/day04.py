# Input: passports separated by blank lines, each with info on
#        birth year (byr), eye colour (ecl), expiration year (eyr), etc.

TEST = """ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in
"""

with open('day04.txt', 'r') as infile:
    PUZZLE = infile.read()

def part1(data):
    """Return how many passports have all info except possibly cid."""
    expected = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
    fields, valid = set(), 0
    for line in data.splitlines():
        if line:    # non-empty line
            fields.update(field[:3] for field in line.split())
        else:       # blank line: check passport and start new one
            valid += expected <= fields
            fields = set()
    return valid + (expected <= fields)   # account for last passport

assert part1(TEST) == 2     # 1st and 3rd passports have 7 fields
print(part1(PUZZLE))

# didn't do Part 2: tedious validation
