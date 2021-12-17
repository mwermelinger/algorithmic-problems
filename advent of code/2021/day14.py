# Input: first line is a start string; after blank line, rules to insert letters

TEST = """NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C"""

# For each pair of adjacent letters, if there's a rule, insert the letter
# between the pair. For TEST, the first rewrite applies rules for NN, NC and CB
# to obtain NCNBCHB.

with open('day14.txt', 'r') as infile:
    PUZZLE = infile.read()

from collections import Counter

def read(data):
    """Return the start string and the rules, as a dictionary."""
    lines = data.splitlines()
    rules = dict()      # one entry XY: L for each rewriting rule XY -> L
    for index in range(2, len(lines)):
        line = lines[index]
        rules[line[:2]] = line[-1]
    return lines[0], rules

def apply(rules, start, n):
    """Return bag of letter pairs after applying rules n times to start.

    String doubles in length with each rewrite, so use a compact representation:
    for each unique pair in the string, count how often it occurs.
    TEST start string NNCB is represented as {'NN': 1, 'NC':1, 'CB': 1}.
    """
    pairs = Counter()
    for index in range(len(start) - 1):
        pairs[start[index:index+2]] += 1

    for _ in range(n):
        new_pairs = Counter()
        for pair in pairs:
            if pair in rules:           # if there's a rule XY -> L
                letter = rules[pair]    # all pairs XY become XL and LY
                new_pairs[pair[0] + letter] += pairs[pair]
                new_pairs[letter + pair[1]] += pairs[pair]
            else:
                new_pairs[pair] = pairs[pair]
        pairs = new_pairs
    return pairs

# Parts 1 and 2 ask for the same

def part(data, n):
    """Return the range of letter frequency after n rewriting steps."""
    start, rules = read(data)
    pairs = apply(rules, start, n)
    frequency = [0] * 26        # frequency of each letter
    A = ord('A')                # ASCII code of letter A
    for pair in pairs:          # count occurrences of first letter in each pair
        frequency[ord(pair[0]) - A] += pairs[pair]
    # rewriting doesn't change first and last letters of string
    # account for last letter in string, which isn't first of any pair
    frequency[ord(start[-1]) - A] += 1
    return max(frequency) - min(f for f in frequency if f != 0)

assert part(TEST, 10) == 1588
print(part(PUZZLE, 10))

assert part(TEST, 40) == 2188189693529
print(part(PUZZLE, 40))
