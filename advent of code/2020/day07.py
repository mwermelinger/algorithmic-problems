# Input: one rule about luggage packing per line

TEST = """light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.
"""

with open('day07.txt', 'r') as infile:
    PUZZLE = infile.read()

import re

def part1(data):
    """Return how many kinds of bag can (in)directly contain a shiny gold bag"""

    def dfs(graph, start):
        """Return the nodes visited by a depth-first search from the start node.

        graph is a dictionary of nodes to their neighbours (adjacency list)
        """
        visited = []
        to_visit = [start]
        while to_visit:
            current = to_visit.pop()
            visited.append(current)
            for neighbour in graph.get(current, []):
                if neighbour not in visited + to_visit:
                    to_visit.append(neighbour)
        return visited

    within = dict() # within[b] = [b1, b2, ...] with all bi that contain b
    for line in data.splitlines():
        container, contained = line.split(' bags contain ')
        for bag in re.findall(r'(\w+ \w+) bags?', contained):
            if bag in within:
                within[bag].append(container)
            else:
                within[bag] = [container]
    return len(dfs(within, 'shiny gold')) - 1

assert part1(TEST) == 4     # gold bag can be in white, yellow, orange, red bags
print(part1(PUZZLE))

def part2(data):
    """Return how many bags are in a shiny gold bag."""
    def packs(graph, bag):
        """Return number of bags inside bag.

        graph is a weighted DAG of the containment relation
        """
        if bag not in graph:    # bag == 'no other'
            return 0

        return sum(qty * (packs(graph, packed) + 1) # include the packed bag
                    for qty, packed in graph[bag])

    contains = dict() # contains[b] = [b1, b2, ...] s.t. b contains bi
    for line in data.splitlines():
        container, contained = line.split(' bags contain ')
        # contained is e.g. '2 red brown bags, 1 purple orchid bag'
        bags = [(int(qty), bag) for
                qty, bag in re.findall(r'(\d+) (\w+ \w+) bags?', contained)]
        if bags:
            contains[container] = bags
    return packs(contains, 'shiny gold')

assert part2(TEST) == 32
# another example in the problem description
assert part2("""shiny gold bags contain 2 dark red bags.
dark red bags contain 2 dark orange bags.
dark orange bags contain 2 dark yellow bags.
dark yellow bags contain 2 dark green bags.
dark green bags contain 2 dark blue bags.
dark blue bags contain 2 dark violet bags.
dark violet bags contain no other bags.""") == 126
print(part2(PUZZLE))
