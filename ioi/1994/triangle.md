# Triangle

Given a triangle of integers with 2 to 100 rows,
find the largest sum from the first to the last row.
From each row to the next we must move left or right.
For example, for the triangle
```
    7
   3 8
  8 1 0
 2 7 4 4
4 5 2 6 5
```
the expected output is 7 + 3 + 8 + 7 + 5 = 30.
Any other path has a lower sum, e.g. 7 + 8 + 1 + 7 + 5 = 28.

The input starts with the number of rows, followed by the triangle, like this:
```python
EXAMPLE = """5
7
3 8
8 1 0
2 7 4 4
4 5 2 6 5"""

OUTPUT = 30
```

## Input
Contestants must read from file `INPUT.TXT` and write to file `OUTPUT.TXT`.
I will read from the example string as if it were a file.
I won't output the result and instead compare it to the expected value.
```python
import io

def integers(line: str):
    """Return the list of integers in the given input line."""
    return [int(string) for string in line.split()]

with io.StringIO(EXAMPLE) as infile:    # instead of open('INPUT.TXT', 'r')
    rows = int(infile.readline())
    triangle = [integers(line) for line in infile]
```

The following approaches are explained in detail in the
[official solutions](https://ioinformatics.org/files/ioi1994solutions.pdf).

## Recursive
The first solution uses top-down recursion and
notes this wouldn't process the larger tests within the time limit.
```python
def max_sum(row, column):
    """Maximal sum for subtree rooted at row and column."""
    root = triangle[row][column]
    below = row + 1
    if below == rows:   # base case: row is the last one
        return root
    left = max_sum(below, column)
    right = max_sum(below, column+1)
    return root + max(left, right)

assert max_sum(0, 0) == OUTPUT
```

## Recursive with memoisation
The second solution computes the sum from each triangle position once
and caches the value in an auxiliary triangular table.
This is sufficient to pass the tests within the time limits.

The official solution initialises the table with -1 in each position,
whereas I use `None` so that arithmetic operations fail in case of a bug.
The important point is to initialise the table with impossible sums.
(The numbers go from 0 to 99 so a sum of 0 is possible.)
```python
# row 0 has 1 column, row 1 has 2 columns, row n has n+1 columns
max_sums = [[None] * (row+1) for row in range(rows)]

def max_sum(row, column):
    """Maximal sum for subtree rooted at row and column."""
    if max_sums[row][column] is None:
        root = triangle[row][column]
        below = row + 1
        if below == rows:
            max_sums[row][column] = root
        else:
            left = max_sum(below, column)
            right = max_sum(below, column+1)
            max_sums[row][column] = root + max(left, right)
    return max_sums[row][column]

assert max_sum(0, 0) == OUTPUT
```

## Bottom-up iterative
The third solution fills the auxiliary table from the bottom up.
```python
max_sums = [[None] * (row+1) for row in range(rows)]

for row in reversed(range(rows)):       # from last row to row 0
    below = row + 1
    for column in range(row+1):         # row 0 has 1 column, row 1 has 2, etc.
        root = triangle[row][column]
        if below == rows:
            max_sums[row][column] = root
        else:
            left = max_sums[below][column]
            right = max_sums[below][column+1]
            max_sums[row][column] = root + max(left, right)

assert max_sums[0][0] == OUTPUT
```
A simpler and more efficient version overwrites the triangle.
```py
for row in reversed(range(rows-1)):     # start in penultimate row
    for column in range(row+1):         
        left = triangle[row+1][column]
        right = triangle[row+1][column+1]
        triangle[row][column] += max(left, right)

assert triangle[0][0] == OUTPUT
```

## Top-down iterative
The fourth solution accumulates the maximum sum of each
possible path to reach the last row read so far. For example,
after reading the first two rows, the maximal sums are `[10, 15]`.
This approach doesn't require to store in memory the whole triangle.

The official solution doesn't provide any code and neither do I.
It's not worth complicating an algorithm to avoid storing a small input
(~5000 integers in the worst case).

## Further exercises
The solution document suggests these variants:

- return the maximal sum path as a sequence of Ls and Rs;
- compute how many paths have the maximal sum;
- compute the mean path sum over all paths.
