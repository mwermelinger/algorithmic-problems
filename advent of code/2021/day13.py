# Input: one dot coordinate per line, then one folding instruction per line

TEST = """6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0

fold along y=7
fold along x=5"""

with open('day13.txt', 'r') as infile:
    PUZZLE = infile.read()

import re

def read(data: str) -> tuple:
    """Return a set of dots and a list of folding instructions."""
    dots = set()
    folds = []
    dot = True
    for line in data.splitlines():
        if not line:
            dot = False     # after an empty line it's foldings, not dots
        elif dot:
            dots.add(tuple(map(int, line.split(','))))
        else:
            axis, value = re.search(r'(.)=(\d+)', line).group(1, 2)
            folds.append( (axis, int(value)) )
    return dots, folds

def fold(dots: set, folding: tuple) -> set:
    """Return set of dots after folding."""
    axis, line = folding
    folded = set()
    for x, y in dots:
        # update x/y coordinate if right of/below the folding line
        if axis == 'x':
            folded.add( (x if x < line else 2*line-x, y))
        else:
            folded.add( (x, y if y < line else 2*line-y))
    return folded

def part1(data):
    """Return how many dots visible after first fold."""
    dots, folds = read(data)
    return len(fold(dots, folds[0]))

assert part1(TEST) == 17
print(part1(PUZZLE))

def part2(data):
    """Print dots after all foldings."""
    dots, folds = read(data)
    for folding in folds:
        dots = fold(dots, folding)
    # create a matrix of spaces, replace some with dots, print each row
    width = max(x for x, y in dots) + 1     # to account for x = 0
    height = max(y for x, y in dots) + 1
    paper = [[' '] * width for _ in range(height)]
    for x, y in dots:
        paper[y][x] = '#'
    for row in paper:
        print(''.join(row))

part2(TEST)     # square of dots: letter O
part2(PUZZLE)   # letters RKHFZGUB
