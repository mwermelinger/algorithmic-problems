# Input: rectangular grid of digits, each the height of the terrain

TEST = """2199943210
3987894921
9856789892
8767896789
9899965678
"""

with open('day09.txt', 'r') as infile:
    PUZZLE = infile.read()

# the next two functions were extracted from part1() after seeing Part 2

def read(data):
    """Return a grid of ints."""
    # put 9s around the input grid to not handle special border cases
    heights = []
    for line in data.splitlines():
        heights.append([9] + list(map(int, line)) + [9])
    length = len(heights[0])
    heights.insert(0, [9] * length)
    heights.append([9] * length)
    return heights

def lowest(r, c, heights):
    """Check if position (r, c) has lower height than all neighbours."""
    height = heights[r][c]
    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        if height >= heights[r+dr][c+dc]:
            return False
    return True

def part1(data):
    """Return sum of risk levels of points lower than their neighbours.

    The risk level is the height + 1.
    """
    heights = read(data)
    risk = 0
    for row in range(1, len(heights) - 1):
        for col in range(1, len(heights[row]) - 1):
            if lowest(row, col, heights):
                risk += heights[row][col] + 1
    return risk

assert part1(TEST) == 15
print(part1(PUZZLE))

import math

def part2(data):
    """Return the product of the sizes of the 3 largest basins.

    A basin is all the points of height < 9 that flow into a low point.
    No point is in two basins. I guess that means input like

    319
    499
    529

    is impossible because 5 would be in 1's and 2's basins.
    """
    def basin(r, c):
        """Return the size of the basin flowing into (r, c).

        Precondition: (r, c) is a lowest point, with height < 9
        """
        visited = set()         # depth-first search of higher positions
        to_visit = [(r, c)]
        while to_visit:
            r, c = to_visit.pop()
            if (r, c) not in visited:
                visited.add( (r, c) )
                height = heights[r][c]
                for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    # I assume there's no flow between equal heights
                    if height < heights[r+dr][c+dc] < 9:
                        to_visit.append( (r+dr, c+dc) )
        return len(visited)

    heights = read(data)
    basins = []
    for row in range(1, len(heights) - 1):
        for col in range(1, len(heights[row]) - 1):
            if lowest(row, col, heights):
                basins.append(basin(row, col))

    return math.prod(sorted(basins)[-3:])

assert part2(TEST) == 1134
print(part2(PUZZLE))
