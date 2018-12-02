print("Advent of Code 2018 - Day 2")


def read_file_lines_list(name):
    input_file = open(name)

    indata = input_file.read()
    indata = indata.splitlines()

    input_file.close()
    return indata


def create_frequency_table(s):
    result = {}
    for c in s:
        result[c] = result[c] + 1 if c in result else 1
    return result


def frequency_table_filter(n):
    def do_filter(tab):
        for key in tab:
            if tab[key] == n:
                return True
        return False

    return do_filter


def string_diff_count(s1, s2):
    i = 0
    diff = 0
    while i < len(s1):
        diff += 1 if s1[i] != s2[i] else 0
        i += 1
    return diff


def string_union(s1, s2):
    result = ""
    ix = 0
    while ix < len(s1):
        result += s1[ix] if s1[ix] == s2[ix] else ""
        ix += 1
    return result


indata = read_file_lines_list("aoc-02-input.txt")

# --- Part One ---

# To make sure you didn't miss any, you scan the likely candidate boxes again, counting the number that have an ID containing exactly two of any letter and then separately counting those with exactly three of any letter. You can multiply those two counts together to get a rudimentary checksum and compare it to what your device predicts.

# For example, if you see the following box IDs:

# abcdef contains no letters that appear exactly two or three times.
# bababc contains two a and three b, so it counts for both.
# abbcde contains two b, but no letter appears exactly three times.
# abcccd contains three c, but no letter appears exactly two times.
# aabcdd contains two a and two d, but it only counts once.
# abcdee contains two e.
# ababab contains three a and three b, but it only counts once.

# Of these box IDs, four of them contain a letter which appears exactly twice, and three of them contain a letter which appears exactly three times. Multiplying these together produces a checksum of 4 * 3 = 12.

# What is the checksum for your list of box IDs?

print("Part 1")

indataFrequencyTables = list(map(create_frequency_table, indata))
indataWith2s = list(filter(frequency_table_filter(2), indataFrequencyTables))
indataWith3s = list(filter(frequency_table_filter(3), indataFrequencyTables))

print("The answer is {0}".format(len(indataWith2s)*len(indataWith3s)))

# 4980 is the right answer

# --- Part Two ---

# Confident that your list of box IDs is complete, you're ready to find the boxes full of prototype fabric.

# The boxes will have IDs which differ by exactly one character at the same position in both strings. For example, given the following box IDs:

# abcde
# fghij
# klmno
# pqrst
# fguij
# axcye
# wvxyz
# The IDs abcde and axcye are close, but they differ by two characters (the second and fourth). However, the IDs fghij and fguij differ by exactly one character, the third (h and u). Those must be the correct boxes.

# What letters are common between the two correct box IDs? (In the example above, this is found by removing the differing character from either ID, producing fgij.)

print("Part 2")


def solvePart2(indata):
    ix = 0
    while ix < len(indata):
        curstr = indata[ix]
        ix2 = 0
        while ix2 < len(indata):
            if ix2 != ix:
                teststr = indata[ix2]
                if string_diff_count(curstr, teststr) == 1:
                    return [curstr, teststr]
            ix2 += 1
        ix += 1


result = solvePart2(indata)

print("The answer is {0}".format(string_union(result[0], result[1])))

# qysdtrkloagnfozuwujmhrbvx is the right answer
