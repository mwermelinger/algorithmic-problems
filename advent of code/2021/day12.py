# Input: one pair of connected caves per line; small caves are in lower case

TEST1 = """start-A
start-b
A-c
A-b
b-d
A-end
b-end"""

TEST2 = """dc-end
HN-start
start-kj
dc-start
dc-HN
LN-dc
HN-end
kj-sa
kj-HN
kj-dc
"""

TEST3 = """fs-end
he-DX
fs-he
start-DX
pj-DX
end-zg
zg-sl
zg-pj
pj-he
RW-he
fs-DX
pj-RW
zg-RW
start-pj
he-WI
zg-he
pj-fs
start-RW"""

with open('day12.txt', 'r') as infile:
    PUZZLE = infile.read()

from collections import defaultdict
import re

def read(data):
    """Return the graph of caves."""
    graph = defaultdict(list)
    for line in data.splitlines():
        node1, node2 = re.match(r'(\w+)-(\w+)', line).group(1, 2)
        graph[node1].append(node2)
        graph[node2].append(node1)
    return graph

def part1(data):
    """Return how many paths from start to end visit small caves once."""

    def paths(node: str, visited: set, path: list) -> int:
        """Return how many paths from node to end don't revisit visited.

        Path ends in node and is for debugging purposes only.
        """
        # Do recursive depth-first traversal, marking small caves as visited.
        # Revisiting large caves doesn't lead to loops because
        # there are no edges between large caves in the data.

        if node == 'end':
            # print(path)
            return 1

        total = 0
        for neighbour in graph[node]:
            if neighbour not in visited:
                new_path = path + [neighbour]
                if neighbour.islower():     # small cave: mark as visited
                    total += paths(neighbour, visited | {neighbour}, new_path)
                else:
                    total += paths(neighbour, visited, new_path)
        return total

    graph = read(data)
    return paths('start', {'start'}, ['start'])

assert part1(TEST1) == 10
assert part1(TEST2) == 19
assert part1(TEST3) == 226
print(part1(PUZZLE))

def part2(data):
    """Return how many paths from start to end visit 0 or 1 small cave twice.

    The start and end caves are visited once only.
    """

    def paths(node:str, visited:set, path:list, twice:str) -> int:
        """Return how many paths from node to end obey the conditions.

        Twice is either '' or the small cave that was visited two times.
        """
        if node == 'end':
            # print(path)
            return 1

        total = 0
        for neighbour in graph[node]:
            new_path = path + [neighbour]
            if neighbour.isupper():             # visit large cave
                total += paths(neighbour, visited, new_path, twice)
            elif neighbour not in visited:      # visit unvisited small cave
                total += paths(neighbour, visited | {neighbour}, new_path, twice)
            elif neighbour != 'start' and not twice:
                # we can visit this small cave again
                total += paths(neighbour, visited, new_path, neighbour)
        return total

    graph = read(data)
    return paths('start', {'start'}, ['start'], '')

assert part2(TEST1) == 36
assert part2(TEST2) == 103
assert part2(TEST3) == 3509
print(part2(PUZZLE))
