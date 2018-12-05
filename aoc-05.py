#!/usr/bin/env python3

import re
from string import ascii_lowercase

print("Advent of Code 2018 - Day 5")


def read_file_lines_list(name):
    with open(name) as f:
        return f.read()


indata = read_file_lines_list("aoc-05-input.txt")
#indata = "dabAcCaCBAcCcaDA"

# --- Day 5: Alchemical Reduction ---

# You've managed to sneak in to the prototype suit manufacturing lab. The Elves are making decent progress, but are still
# struggling with the suit's size reduction capabilities.

# While the very latest in 1518 alchemical technology might have solved their problem eventually, you can do better. You
# scan the chemical composition of the suit's material and discover that it is formed by extremely long polymers
# (one of which is available as your puzzle input).

# The polymer is formed by smaller units which, when triggered, react with each other such that two adjacent units of
# the same type and opposite polarity are destroyed. Units' types are represented by letters; units' polarity is
# represented by capitalization. For instance, r and R are units with the same type but opposite polarity, whereas r and
# s are entirely different types and do not react.

# For example:

# In aA, a and A react, leaving nothing behind.
# In abBA, bB destroys itself, leaving aA. As above, this then destroys itself, leaving nothing.
# In abAB, no two adjacent units are of the same type, and so nothing happens.
# In aabAAB, even though aa and AA are of the same type, their polarities match, and so nothing happens.

# Now, consider a larger example, dabAcCaCBAcCcaDA:

# dabAcCaCBAcCcaDA  The first 'cC' is removed.
# dabAaCBAcCcaDA    This creates 'Aa', which is removed.
# dabCBAcCcaDA      Either 'cC' or 'Cc' are removed (the result is the same).
# dabCBAcaDA        No further actions can be taken.
# After all possible reactions, the resulting polymer contains 10 units.

# How many units remain after fully reacting the polymer you scanned?


def solve_part_1(s):
    stack = []
    for c1 in s:
        if len(stack) == 0:
            stack.append(c1)
        else:
            c2 = stack.pop()
            if not (((c1.isupper() and c2.islower()) or (c1.islower() and c2.isupper())) and (c1.lower() == c2.lower())):
                stack.append(c2)
                stack.append(c1)
    return len(stack)


print("Part 1")
print("The answer is {0}".format(solve_part_1(indata)))

# 11194 is the right answer

# --- Part Two ---

# Time to improve the polymer.

# One of the unit types is causing problems; it's preventing the polymer from collapsing as much as it should. Your goal
# is to figure out which unit type is causing the most problems, remove all instances of it (regardless of polarity), fully
# react the remaining polymer, and measure its length.

# For example, again using the polymer dabAcCaCBAcCcaDA from above:

# Removing all A/a units produces dbcCCBcCcD. Fully reacting this polymer produces dbCBcD, which has length 6.
# Removing all B/b units produces daAcCaCAcCcaDA. Fully reacting this polymer produces daCAcaDA, which has length 8.
# Removing all C/c units produces dabAaBAaDA. Fully reacting this polymer produces daDA, which has length 4.
# Removing all D/d units produces abAcCaCBAcCcaA. Fully reacting this polymer produces abCBAc, which has length 6.
# In this example, removing all C/c units was best, producing the answer 4.

# What is the length of the shortest polymer you can produce by removing all units of exactly one type and fully reacting the result?


def solve_part_2(s):
    min_length = 99999
    orig_len = len(s)
    for ch in ascii_lowercase:
        regexp = re.compile(ch, re.IGNORECASE)
        s2 = regexp.sub("", s)
        new_len = len(s2)
        if new_len != orig_len:
            length = solve_part_1(s2)
            if length < min_length:
                min_length = length
    return min_length


print("Part 2")
print("The answer is {0}".format(solve_part_2(indata)))

# 4178 is the right answer
