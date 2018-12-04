#!/usr/bin/env python3

import re

print("Advent of Code 2018 - Day 3")


def read_file_lines_list(name):
    input_file = open(name)

    indata = input_file.read()
    indata = indata.splitlines()

    input_file.close()
    return indata


def parse_claim(line):
    match = re.match('^#(\\d+) @ (\\d+),(\\d+): (\\d+)x(\\d+)$', line)
    claim = {
        "id": int(match.group(1)),
        "left": int(match.group(2)),
        "top": int(match.group(3)),
        "width": int(match.group(4)),
        "height": int(match.group(5))
    }
    claim["xrange"] = list(
        range(claim["left"] + 1, claim["width"] + claim["left"] + 1))
    claim["yrange"] = list(
        range(claim["top"] + 1, claim["height"] + claim["top"] + 1))
    return claim


indata = read_file_lines_list("aoc-03-input.txt")

# --- Part One ---

# The Elves managed to locate the chimney-squeeze prototype fabric for Santa's suit (thanks to someone who helpfully wrote
# its box IDs on the wall of the warehouse in the middle of the night). Unfortunately, anomalies are still affecting them -
# nobody can even agree on how to cut the fabric.

# The whole piece of fabric they're working on is a very large square - at least 1000 inches on each side.

# Each Elf has made a claim about which area of fabric would be ideal for Santa's suit. All claims have an ID and consist
# of a single rectangle with edges parallel to the edges of the fabric. Each claim's rectangle is defined as follows:

# The number of inches between the left edge of the fabric and the left edge of the rectangle.
# The number of inches between the top edge of the fabric and the top edge of the rectangle.
# The width of the rectangle in inches.
# The height of the rectangle in inches.

# A claim like #123 @ 3,2: 5x4 means that claim ID 123 specifies a rectangle 3 inches from the left edge, 2 inches from
# the top edge, 5 inches wide, and 4 inches tall. Visually, it claims the square inches of fabric represented by # (and
# ignores the square inches of fabric represented by .) in the diagram below:

# ...........
# ...........
# ...#####...
# ...#####...
# ...#####...
# ...#####...
# ...........
# ...........
# ...........

# The problem is that many of the claims overlap, causing two or more claims to cover part of the same areas.
# For example, consider the following claims:

# #1 @ 1,3: 4x4
# #2 @ 3,1: 4x4
# #3 @ 5,5: 2x2

# Visually, these claim the following areas:

# ........
# ...2222.
# ...2222.
# .11XX22.
# .11XX22.
# .111133.
# .111133.
# ........

# The four square inches marked with X are claimed by both 1 and 2. (Claim 3, while adjacent to the others,
# does not overlap either of them.)

# If the Elves all proceed with their own plans, none of them will have enough fabric.
# How many square inches of fabric are within two or more claims?

print("Part 1")

claims = list(map(parse_claim, indata))
seen = {}

for claim in claims:
    for x in claim["xrange"]:
        for y in claim["yrange"]:
            key = "{0}:{1}".format(x, y)
            seen[key] = seen[key] + 1 if key in seen else 1

result = 0
for key in seen:
    if seen[key] > 1:
        result += 1

print("The answer is {0}".format(result))

# 115242 is the right answer

# --- Part Two ---

# Amidst the chaos, you notice that exactly one claim doesn't overlap by even a single square inch of
# fabric with any other claim. If you can somehow draw attention to it, maybe the Elves will be able
# to make Santa's suit after all!

# For example, in the claims above, only claim 3 is intact after all claims are made.

# What is the ID of the only claim that doesn't overlap?

print("Part 2")


def solve_part_2():
    for claim in claims:
        overlapping = False
        for x in claim["xrange"]:
            for y in claim["yrange"]:
                if seen["{0}:{1}".format(x, y)] > 1:
                    overlapping = True
        if not overlapping:
            return claim['id']


print("The answer is {0}".format(solve_part_2()))

# 1046 is the right answer
