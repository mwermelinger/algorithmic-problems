# Input: one integer per line

TEST = """199
200
208
210
200
207
240
269
260
263"""

with open('day01.txt', 'r') as infile:
    PUZZLE = infile.read()

def part1(data):
    """Return how often there's an increase from a number to the next."""
    numbers = list(map(int, data.splitlines()))
    return sum(numbers[i-1] < numbers[i] for i in range(1, len(numbers)))

assert part1(TEST) == 7
print(part1(PUZZLE))

def part2(data):
    """Return how often the sum of 3 consecutive numbers increases."""
    numbers = list(map(int, data.splitlines()))
    return sum(sum(numbers[i-1:i+2]) < sum(numbers[i:i+3])
                for i in range(1, len(numbers) - 2))

assert part2(TEST) == 5
print(part2(PUZZLE))
