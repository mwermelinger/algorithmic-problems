# Input: one integer per line, representing an expense

TEST = """1721
979
366
299
675
1456"""

with open('day01.txt', 'r') as infile:
    PUZZLE = infile.read()

def part1(data):
    """Return the product of 2 numbers that add to 2020"""
    # text says 'two entries' so I assume different numbers are added
    numbers = tuple(map(int, data.splitlines()))
    for first in range(len(numbers)-1):
        for second in range(first+1, len(numbers)):
            if numbers[first] + numbers[second] == 2020:
                return numbers[first] * numbers[second]

assert part1(TEST) == 514579
print(part1(PUZZLE))

def part2(data):
    """Return the product of 3 numbers that add to 2020"""
    # could reduce search space by assuming numbers (expenses) are positive
    numbers = tuple(map(int, data.splitlines()))
    for first in range(len(numbers)-2):
        for second in range(first+1, len(numbers)-1):
            for third in range(second+1, len(numbers)):
                if numbers[first] + numbers[second] + numbers[third] == 2020:
                    return numbers[first] * numbers[second] * numbers[third]

assert part2(TEST) == 241861950
print(part2(PUZZLE))
