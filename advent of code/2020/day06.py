# Input: one line per person, with questions answered
#        blank lines separate groups of people

TEST = """abc

a
b
c

ab
ac

a
a
a
a

b
"""

with open('day06.txt', 'r') as infile:
    PUZZLE = infile.read()

def part1(data):
    """Return how many questions answered by anyone in each group."""
    questions, count = set(), 0
    for line in data.splitlines():
        if line:
            questions |= set(line)
        else:       # blank line: count answers for this group, start new one
            count += len(questions)
            questions = set()
    return count + len(questions)   # process last group

assert part1(TEST) == 3 + 3 + 3 + 1 + 1     # first three groups answer a, b, c
print(part1(PUZZLE))

import string

def part2(data):
    """Return how many questions answered by everyone in each group."""
    questions, count = set(string.ascii_lowercase), 0
    for line in data.splitlines():
        if line:
            questions &= set(line)
        else:
            count += len(questions)
            questions = set(string.ascii_lowercase)
    return count + len(questions)   # process last group

assert part2(TEST) == 3 + 0 + 1 + 1 + 1     # 2nd group: all answer differently
print(part2(PUZZLE))
