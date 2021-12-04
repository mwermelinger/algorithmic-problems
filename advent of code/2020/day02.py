# Input: lines of the form int-int character: string

TEST = """1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc"""

with open('day02.txt', 'r') as infile:
    PUZZLE = infile.read()

import re

def part1(data):
    """Return how many passwords are valid.

    min-max letter: pwd => pwd is valid if letter occurs min to max times
    """
    def is_valid(line):
        """Check if a letter's occurrences are within a given range."""
        match = re.match(r'(\d+)-(\d+) (.): (.*)', line)
        min, max, letter, pwd = match.group(1, 2, 3, 4)
        return int(min) <= pwd.count(letter) <= int(max)

    return sum(is_valid(line) for line in data.splitlines())

assert part1(TEST) == 2
print(part1(PUZZLE))

def part2(data):
    """Return how many passwords are valid.

    low-high letter: pwd => pwd is valid if letter is in one of two positions
    """
    def is_valid(line):
        """Check if letter occurs in only one of two 1-based positions."""
        match = re.match(r'(\d+)-(\d+) (.): (.*)', line)
        low, high, letter, pwd = match.group(1, 2, 3, 4)
        return (pwd[int(low) - 1] == letter) ^ (pwd[int(high) - 1] == letter)

    return sum(is_valid(line) for line in data.splitlines())

assert part2(TEST) == 1
print(part2(PUZZLE))
