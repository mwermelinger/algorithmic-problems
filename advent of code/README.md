# Advent of Code

The [Advent of Code](https://adventofcode.com/about) is
an advent calendar with a programming puzzle every day.
Each puzzle consists of two parts that use the same input data.
We can use any language and programming environment, as we're only asked to
submit the answer to each part, which is usually a single integer.
Different users may get different input data to prevent copying answers.

The second part is revealed only after submitting the first part's answer.
I don't change my first part's code in light of the second part.

For most problems, my routine is:

1. Copy the `day00.py` template to `dayDD.py` where `DD` is the current day.
1. On the AoC problem page, click on the link to my input data and save it to file `dayDD.txt`.
1. Paste the example input given on the AoC problem page into string `TEST`.
1. For the example input, write the expected output after the `assert` for part 1.
1. Write, run and debug function `part1` until the assertion is silent (no exception).
1. Copy the printed output to the AoC website to unlock part 2.
1. Repeat steps 4-6 for part 2.
