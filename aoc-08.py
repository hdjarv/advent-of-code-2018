#!/usr/bin/env python3

from functools import reduce


def parse_node(data, ix):
    node = {}
    node["children"] = list(range(data[ix]))
    ix += 1
    node["metadata"] = list(range(data[ix]))
    ix += 1
    for i in node["children"]:
        (node["children"][i], ix) = parse_node(data, ix)
    for i in node["metadata"]:
        node["metadata"][i] = data[ix]
        ix += 1
    return (node, ix)


def walk_node(node, cb, data=None, depth=0):
    cb(node, data, depth)
    for ch in node["children"]:
        walk_node(ch, cb, data, depth+1)


def print_node(node):
    def __print_node__(node, dummy, depth):
        print((" "*depth) +
              " -- node: {0}, {1}".format(len(node["children"]), len(node["metadata"])))
        print((" "*depth) + "  metadata:")
        for m in node["metadata"]:
            print((" "*depth) + "    " + str(m))

    walk_node(node, __print_node__, None)


def sum_node_metadata(node):
    return reduce(lambda s, v: s+v, node["metadata"])


def solve_part_1(data):
    def __sum_metadata__(node, result, dummy):
        result["value"] += sum_node_metadata(node)

    node = parse_node(data, 0)[0]
    result = {"value": 0}
    walk_node(node, __sum_metadata__, result)

    return result["value"]


def calc_node_value(node):
    if len(node["children"]) == 0:
        return sum_node_metadata(node)
    else:
        result = 0
        for ix in node["metadata"]:
            if ix != 0 and ix-1 < len(node["children"]):
                result += calc_node_value(node["children"][ix-1])
        return result


def solve_part_2(data):
    node = parse_node(data, 0)[0]
    return calc_node_value(node)


with open("aoc-08-input.txt") as f:
    data = f.read().splitlines()
    f.close()

    data = list(map(lambda l: list(map(lambda s: int(s), l.split())), data))[0]

    print("Advent of Code 2018 - Day 8")
    print("Part 1: The answer is {0}".format(solve_part_1(data)))
    #  38722 is the right answer
    print("Part 2: The answer is {0}".format(solve_part_2(data)))
    #  13935 is the right answer
