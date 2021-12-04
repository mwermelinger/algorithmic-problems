# Input: a grid with trees (#) and open terrain (.)

TEST = """..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#"""

with open('day03.txt', 'r') as infile:
    PUZZLE = infile.read()

def part1(data):
    """Return how many trees are hit when travelling 1 down and 3 to the right.

    The start position is the top left corner, open terrain.
    The grid repeats infinitely to the right.
    """
    terrain = data.splitlines()
    column, trees = 3, 0
    for row in range(1, len(terrain)):
        line = terrain[row]
        trees += line[column % len(line)] == '#'
        column += 3
    return trees

assert part1(TEST) == 7
print(part1(PUZZLE))

def part2(data):
    """Find the product of trees hit in 5 runs at different slopes."""
    terrain = data.splitlines()
    product = 1
    for dc, dr in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]:
        column, trees = dc, 0
        for row in range(dr, len(terrain), dr):
            line = terrain[row]
            trees += line[column % len(line)] == '#'
            column += dc
        product *= trees
    return product

assert part2(TEST) == 336
print(part2(PUZZLE))
