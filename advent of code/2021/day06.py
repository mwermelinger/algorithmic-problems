# Input: comma-separated numbers from 0 to 8
#        each number is the number of days until that fish spawns another

TEST = """3,4,3,1,2"""

with open('day06.txt', 'r') as infile:
    PUZZLE = infile.read()

from collections import Counter, deque

def part1(data, days):
    """Return how many fish there are after the given days."""
    fish = Counter(data)        # count the fish for each number of days
    population = deque()        # a queue of fish at each stage (0 to 8)
    for day in '012345678':
        population.append(fish[day])
    for _ in range(days):
        day0 = population.popleft()
        population[6] += day0    # fish take another 7 days to reproduce
        population.append(day0)  # each fish has one descendant
    return sum(population)

assert part1(TEST, 80) == 5934
print(part1(PUZZLE, 80))

# Part 2 is the same question, just over a longer time period

assert part1(TEST, 256) == 26984457539
print(part1(PUZZLE, 256))
