# Input: one binary number per line. The number of digits isn't stated.

TEST = """00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010"""

with open('day03.txt', 'r') as infile:
    PUZZLE = infile.read()

def part1(data):
    """Multiply the gamma and epsilon rates.

    They're the binary numbers formed from the
    most resp. least frequent bit at each position.
    """
    lines = data.splitlines()
    bits = len(lines[0])

    # compute how many zeros in each position
    zeros = [0] * bits
    for line in lines:
        for index, bit in enumerate(line):
            if bit == '0':
                zeros[index] += 1

    # create gamma by taking most frequent bit at each position
    gamma = ''
    half = len(lines) // 2
    for count in zeros:
        gamma += '0' if count > half else '1'

    # epsilon uses least frequent bit, so it's the complement of gamma
    gamma = int(gamma, 2)                   # convert to decimal
    epsilon = (2 ** bits - 1) - gamma       # in binary: 111...1 - gamma
    return gamma * epsilon

assert part1(TEST) == 198
print(part1(PUZZLE))


def part2(data):
    """Multiply the oxygen generator rating with the CO2 scrubber rating.

    They are obtained by considering, for each bit position,
    the numbers that have the most resp. least frequent bit at that position and eliminating the others.
    If the 0 and 1 are equally frequent at a position,
    take the numbers with 1 resp. 0 at that position.
    The rating is the last number remaining.
    """

    def rating(numbers, oxygen: bool):
        """Return rating for the given gas."""
        pos = 0
        while len(numbers) > 1:
            # count 0s and 1s at position pos
            zeros = sum(number[pos] == '0' for number in numbers)
            ones = len(numbers) - zeros
            if oxygen:          # use most frequent bit or 1 if a tie
                bit = '0' if zeros > ones else '1'
            else:               # use least frequent bit or 0 if a tie
                bit = '0' if zeros <= ones else '1'
            # get the numbers with that bit at that position
            numbers = [number for number in numbers if number[pos] == bit]
            pos += 1
        return int(numbers[0], 2)

    lines = data.splitlines()
    return rating(lines, True) * rating(lines, False)

assert part2(TEST) == 230
print(part2(PUZZLE))
