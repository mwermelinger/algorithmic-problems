# Input: one integer per line, the mass of each spacecraft module

TEST = """12
14
1969
100756
"""

with open('day01.txt', 'r') as infile:
    PUZZLE = infile.read()

def part1(data):
    """Return the total fuel needed to launch the spacecraft.

    The fuel for a module with mass m is floor(m/3) - 2.
    """
    return sum(int(line) // 3 - 2 for line in data.splitlines())

assert part1(TEST) == 2 + 2 + 654 + 33583   # values in problem description
print(part1(PUZZLE))

def part2(data):
    """As part 1, but take into account the mass of the fuel.

    If a module requires f fuel, carrying that fuel on board
    requires extra floor(f/3) - 2 fuel, which in turn requires extra fuel, etc.
    """
    def fuel(mass):
        this_fuel = mass // 3 - 2
        if this_fuel <= 0:
            return 0
        return this_fuel + fuel(this_fuel)

    return sum(fuel(int(line)) for line in data.splitlines())

assert part2(TEST) == 2 + 2 + 966 + 50346
print(part2(PUZZLE))
