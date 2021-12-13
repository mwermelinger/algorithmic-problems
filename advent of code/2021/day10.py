# Input: one bracket expression per line

TEST = """[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]
"""

with open('day10.txt', 'r') as infile:
    PUZZLE = infile.read()

def part1(data):
    """Add the value of the first invalid bracket in each line."""

    def wrong(line):
        """Return the first wrong closing bracket."""
        open = []   # stack of currently open brackets
        opened = {']': '[', ')': '(', '}': '{', '>': '<'}
        for bracket in line:
            if bracket in '([{<':
                open.append(bracket)
            elif open and opened[bracket] == open[-1]:
                open.pop()
            else:
                return bracket
        return ''   # no invalid closing bracket

    value = {'': 0, ')': 3, ']': 57, '}': 1197, '>': 25137}
    return sum(value[wrong(line)] for line in data.splitlines())

assert part1(TEST) == 26397
print(part1(PUZZLE))

def part2(data):
    """Return the median of the scores of the incomplete lines.

    Preconditions: there's an odd number of incomplete lines
    """

    def complete(line):
        """Return the completion of the line."""
        to_close = []       # stack of currently expected closing brackets
        closed = {'[': ']', '(': ')', '{': '}', '<': '>'}
        for bracket in line:
            if bracket in '([{<':
                to_close.append(closed[bracket])
            elif to_close and bracket == to_close[-1]:
                to_close.pop()
            else:
                return ''   # wrong bracket, no completion possible
        return ''.join(to_close[::-1])  # return closing brackets in reverse

    value = {')': 1, ']': 2, '}': 3, '>': 4}
    scores = []
    for line in data.splitlines():
        score = 0
        for bracket in complete(line):
            score = score * 5 + value[bracket]
        if score:           # wrong lines have score 0 and are ignored
            scores.append(score)
    return sorted(scores)[len(scores) // 2]

assert part2(TEST) == 288957
print(part2(PUZZLE))
