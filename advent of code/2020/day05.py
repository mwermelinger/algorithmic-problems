# Input: one string per line, representing row and column of a plane seat
# ...F and ...B - seat is in front/back half of rows determined by ...
# ...L and ...R - seat is in left/right half of columns determined by ...
# plane as 128 rows and 8 columns

TEST = """FBFBBFFRLR
BFFFBBFRRR
FFFBBBFRRR
BBFFBBFRLL
"""

with open('day05.txt', 'r') as infile:
    PUZZLE = infile.read()

def seat_number(seat):
    """Return the consecutive seat number (8 seats per row)."""
    rows, columns = list(range(128)), list(range(8))
    for character in seat:
        if character == 'F':
            rows = rows[:len(rows) // 2]
        elif character == 'B':
            rows = rows[len(rows) // 2:]
        elif character == 'R':
            columns = columns[len(columns) // 2:]
        else:
            columns = columns[:len(columns) // 2]
    return 8 * rows[0] + columns[0]

def part1(data):
    """Find highest seat number"""
    return max(seat_number(seat) for seat in data.splitlines())

assert part1(TEST) == max(357, 567, 119, 820)
print(part1(PUZZLE))

def part2(data):
    """Return single missing seat number among the range on the plane."""
    seats = {seat_number(seat) for seat in data.splitlines()}
    return set(range(min(seats), max(seats) + 1)) - seats

# more efficient in terms of memory and time
def part2(data):
    """Return single missing seat number among the range on the plane."""
    seats = [seat_number(seat) for seat in data.splitlines()]
    seats.sort()
    previous = seats[0]
    for seat in seats[1:]:
        if seat != previous + 1:
            return previous + 1
        previous = seat

print(part2(PUZZLE))
