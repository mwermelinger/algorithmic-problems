# Input: a comma-separated list of integers, representing a program and its data

TEST = "1,9,10,3,2,3,11,0,99,30,40,50"

with open('day02.txt', 'r') as infile:
    PUZZLE = infile.read()

def part1(data):
    """Return the value at position 0 after running the program.

    Put 12 and 2 in positions 1 and 2 before running. Instructions are:
    1, x, y, r - add the values at positions x and y and put result at r
    2, x, y, r - multiply instead of adding
    99         - halt the execution
    """
    program = data.split(',')
    for index in range(len(program)):
        program[index] = int(program[index])
    # Test data has no position 12 and shouldn't be changed
    if len(program) > 12:
        program[1] = 12
        program[2] = 2
    index = 0
    operation = program[index]
    while operation != 99:
        input1 = program[index + 1]
        input2 = program[index + 2]
        output = program[index + 3]
        if operation == 1:
            program[output] = program[input1] + program[input2]
        else:
            program[output] = program[input1] * program[input2]
        index += 4
        operation = program[index]
    return program[0]

assert part1(TEST) == 3500
assert part1("1,0,0,0,99") == 2             # p[0] = p[0] + p[0] = 1 + 1 = 2
assert part1("2,3,0,3,99") == 2             # p[3] = p[3] * p[0] = 3 * 2 = 6
assert part1("1,1,1,4,99,5,6,0,99") == 30   # p[4] = p[1] + p[1] = 1 + 1 = 2
                                            # p[0] = p[5] * p[6] = 5 * 6 = 30
print(part1(PUZZLE))

def part2(data):
    """Return 100 * x + y where x and y in positions 1 and 2
    make the program halt with 19690720 in position 0.

    In the problem description, x and y are called noun and verb.
    The values will be between 0 and 99, inclusive.
    """
    def result(memory, noun, verb):
        memory[1] = noun
        memory[2] = verb
        ip = 0  # instruction pointer
        opcode = memory[ip]
        while opcode != 99:
            parameter1 = memory[ip+1]
            parameter2 = memory[ip+2]
            parameter3 = memory[ip+3]
            if opcode == 1:
                memory[parameter3] = memory[parameter1] + memory[parameter2]
            else:
                memory[parameter3] = memory[parameter1] * memory[parameter2]
            ip += 4
            opcode = memory[ip]
        return memory[0]

    program = data.split(',')
    for index in range(len(program)):
        program[index] = int(program[index])

    # exhaustive search for the two values
    for noun in range(100):
        for verb in range(100):
            # each run modifies the program, so use a copy of the original one
            if result(program.copy(), noun, verb) == 19690720:
                return 100*noun + verb

print(part2(PUZZLE))
