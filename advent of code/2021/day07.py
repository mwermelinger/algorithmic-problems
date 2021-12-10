# Input: comma-separated numbers, which represent positions of submarines

TEST = """16,1,2,0,4,2,7,1,2,14"""

with open('day07.txt', 'r') as infile:
    PUZZLE = infile.read()

def part1(data):
    """Return least fuel to move all submarines to same position.

    Fuel to go from current position c to desired position d is abs(d - c).
    """
    numbers = list(map(int, data.split(',')))
    numbers.sort()
    n = len(numbers)
    middle = n // 2
    if n % 2:       # odd length
        median = numbers[middle]
    else:
        median = (numbers[middle - 1] + numbers[middle]) // 2
    return sum(abs(number - median) for number in numbers)

assert part1(TEST) == 37
print(part1(PUZZLE))

import math

def part2(data):
    """Return least fuel to move all submarines to same position.

    Fuel to go from current to desired position is 1 + 2 + ... + abs(d - c).
    """
    numbers = list(map(int, data.split(',')))
    # puzzle has 100s of numbers in a range of 1000, so brute-force is OK
    min_fuel = math.inf
    for position in range(min(numbers), max(numbers)+1):
        fuel = 0
        for number in numbers:
            difference = abs(number - position)
            fuel += difference * (difference + 1) // 2
        if fuel < min_fuel:
            min_fuel = fuel
    return min_fuel

assert part2(TEST) == 168
print(part2(PUZZLE))
