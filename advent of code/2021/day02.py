# Input: one command to the submarine per line

TEST = """forward 5
down 5
forward 8
up 3
down 8
forward 2"""

with open('day02.txt', 'r') as infile:
    PUZZLE = infile.read()

def part1(data):
    """Return x*y where (x, y) is the final submarine position.

    The submarine starts at (0, 0). Forward/up/down do the obvious.
    """
    x = y = 0
    for command in data.splitlines():
        instruction, displacement = command.split()
        if instruction == 'forward':
            x += int(displacement)
        elif instruction == 'up':
            y -= int(displacement)
        elif instruction == 'down':
            y += int(displacement)
    return x * y

assert part1(TEST) == 150
print(part1(PUZZLE))

def part2(data):
    """Return x*y where (x, y) is the final submarine position.

    The submarine starts at (0, 0).
    Up/down decreases/increases the aim, which starts at 0.
    The forward n command increases x by n and y by aim * n.
    """
    x = y = aim = 0
    for command in data.splitlines():
        instruction, displacement = command.split()
        displacement = int(displacement)
        if instruction == 'forward':
            x += displacement
            y += aim * displacement
        elif instruction == 'up':
            aim -= displacement
        elif instruction == 'down':
            aim += displacement
    return x * y

assert part2(TEST) == 900
print(part2(PUZZLE))
