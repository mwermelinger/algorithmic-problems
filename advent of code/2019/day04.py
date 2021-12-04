# Input: a range of two 6-digit integers, which represent passwords

PUZZLE = "156218-652527"

"""Part 1

Find how many passwords (numbers in the given range) satisfy these conditions:

- the digits never decrease from left to right
- at least two adjacent digits are the same
"""

passwords = 0
for n in range(156218, 652527+1):
    digits = list(str(n))
    if sorted(digits) == digits and len(set(digits)) != len(digits):
        passwords += 1
print(passwords)

"""Part 2: as part 1 but at least one digit occurs exactly twice."""

from collections import Counter

passwords = 0
debug = False
for n in range(156218, 160000 if debug else 652527+1):
    digits = list(str(n))
    if sorted(digits) == digits:
        if 2 in Counter(digits).values():
            passwords += 1
            if debug: print(n)
print(passwords)
