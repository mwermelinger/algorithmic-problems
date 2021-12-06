# Input: one vent line x1,y1 -> x2,y2 per input line
#        there are vents at every (x,y) along each line

TEST = """0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2"""

# the puzzle data has 3-digit coordinates
with open('day05.txt', 'r') as infile:
    PUZZLE = infile.read()

import re

# My submission used x/y as row/column coordinate, so the points grid was
# rotated by 90 degrees wrt to the grid shown in the problem description.
# A rotated grid doesn't affect the answer to this puzzle, but for consistency
# I've subsequently swapped the coordinates (x = column, y = row).

def part1(data):
    """Return how many points are covered by at least two vent lines.

    Only consider horizontal and vertical lines.
    """
    points = [ [0]*1000 for _ in range(1000) ]
    for line in data.splitlines():
        match = re.match(r'(\d+),(\d+) -> (\d+),(\d+)', line)
        x1, y1, x2, y2 = (int(match.group(i)) for i in range(1, 5))
        if x1 == x2:        # vertical line
            ys = range(y1, y2+1) if y1 <= y2 else range(y2, y1+1)
            for y in ys:
                points[y][x1] += 1
        elif y1 == y2:      # horizontal line
            xs = range(x1, x2+1) if x1 < x2 else range(x2, x1+1)
            for x in xs:
                points[y1][x] += 1
    return sum(points[y][x] > 1 for y in range(1000) for x in range(1000))

assert part1(TEST) == 5
print(part1(PUZZLE))

def part2(data):
    """Return how many points are covered by at least two vent lines.

    Consider also diagonal lines.
    """
    points = [ [0]*1000 for _ in range(1000) ]
    for line in data.splitlines():
        match = re.match(r'(\d+),(\d+) -> (\d+),(\d+)', line)
        x1, y1, x2, y2 = (int(match.group(i)) for i in range(1, 5))
        xs = range(x1, x2+1) if x1 <= x2 else range(x1, x2-1, -1)
        ys = range(y1, y2+1) if y1 <= y2 else range(y1, y2-1, -1)
        if x1 == x2:        # vertical line
            for y in ys:
                points[y][x1] += 1
        elif y1 == y2:      # horizontal line
            for x in xs:
                points[y1][x] += 1
        else:
            for x, y in zip(xs, ys):
                points[y][x] += 1
    return sum(points[y][x] > 1 for y in range(1000) for x in range(1000))

assert part2(TEST) == 12
print(part2(PUZZLE))
