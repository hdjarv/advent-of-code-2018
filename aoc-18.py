#!/usr/bin/env python3

from copy import deepcopy


def count_acre_type(data, typ):
    result = 0
    for line in range(len(data)):
        for col in range(len(data[line])):
            if data[line][col] == typ:
                result += 1
    return result


def count_neighbor_type(data, line, col, typ):
    result = 0
    for l in [line-1, line, line+1]:
        for c in [col-1, col, col+1]:
            if (not (l == line and c == col)) and l >= 0 and l < len(data) and c >= 0 and c < len(data[l]) and data[l][c] == typ:
                result += 1
    return result


def evolve(data):
    newdata = deepcopy(data)
    for line in range(len(data)):
        for col in range(len(data[line])):
            if data[line][col] == '.':
                newdata[line][col] = '|' if count_neighbor_type(
                    data, line, col, '|') >= 3 else '.'
            elif data[line][col] == '|':
                newdata[line][col] = '#' if count_neighbor_type(
                    data, line, col, '#') >= 3 else '|'
            elif data[line][col] == '#':
                newdata[line][col] = '#' if count_neighbor_type(
                    data, line, col, '#') >= 1 and count_neighbor_type(data, line, col, '|') >= 1 else '.'

    return newdata


def solve_part_1(data, minutes=10):
    minute = 0
    while minute < minutes:
        data = evolve(data)
        minute += 1

    lumberyards = count_acre_type(data, '#')
    wooden = count_acre_type(data, '|')

    return lumberyards * wooden


def get_id(data):
    return "".join(map(lambda row: "".join(row), data))


def detect_cycle(data):
    ids = {}
    i = 0
    while True:
        data = evolve(data)
        dataid = get_id(data)
        if dataid in ids:
            return (ids[dataid], i)
        ids[dataid] = i
        i += 1


def solve_part_2(data):
    (from_ix, to_ix) = detect_cycle(data)
    cycle_len = to_ix - from_ix
    left = (1000000000 - from_ix) % cycle_len
    return solve_part_1(data, from_ix+left)


with open("aoc-18-input.txt") as f:
    data = list(map(lambda v: list(v), f.read().splitlines()))

    print("Advent of Code 2018 - Day 18")
    print("Part 1: The answer is {0}".format(solve_part_1(data)))
    print("Part 2: The answer is {0}".format(solve_part_2(data)))
