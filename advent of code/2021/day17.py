# Input: one line describing rectangular target area

TEST = 'target area: x=20..30, y=-10..-5'
PUZZLE = 'target area: x=156..202, y=-110..-69'

import re

def highest(dx, dy, xlo, xhi, ylo, yhi):
    """Return highest y reached with initial dx, dy velocity.

    Return -1 if probe doesn't hit target area"""
    x = y = maxy = 0    # initial probe coordinates and highest height
    hit = False         # I assume probe doesn't start within target area

    # stop moving probe when it hits target or moves past it
    while not hit and (x <= xhi and ylo <= y):
        x += dx
        y += dy
        if dx > 0: dx -= 1          # drag reduces dx; once dx = 0 it stays 0
        dy -= 1                     # gravity decreases dy
        hit = xlo <= x <= xhi and ylo <= y <= yhi
        maxy = max(maxy, y)
    return maxy if hit else -1

def part1(data):
    """Return highest y reached while still hitting the target area."""
    xlo, xhi = map(int, re.search(r'x=([-\d]+)..([-\d]+)', data).group(1, 2))
    ylo, yhi = map(int, re.search(r'y=([-\d]+)..([-\d]+)', data).group(1, 2))
    # as per input data, I assume 0 < xlo and yhi < 0
    maxy = 0
    # I assume 0 < xlo, so dx must be positive to reach area
    # dx <= xhi or else probe overshoots target in first movement
    for dx in range(1, xhi+1):
        # dy >= ylo or else probe overshoots target in first movement
        # dy < -ylo was an educated guess; works for this data
        for dy in range(ylo, -ylo):
            maxy = max(maxy, highest(dx, dy, xlo, xhi, ylo, yhi))
    return maxy


assert part1(TEST) == 45
print(part1(PUZZLE))

def part2(data):
    """Return how many initial velocities lead to hitting the target."""
    xlo, xhi = map(int, re.search(r'x=([-\d]+)..([-\d]+)', data).group(1, 2))
    ylo, yhi = map(int, re.search(r'y=([-\d]+)..([-\d]+)', data).group(1, 2))

    count = 0
    for dx in range(1, xhi+1):
        for dy in range(ylo, -ylo):
            if highest(dx, dy, xlo, xhi, ylo, yhi) != -1:
                count += 1
    return count

assert part2(TEST) == 112
print(part2(PUZZLE))
