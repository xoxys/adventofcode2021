#!/usr/bin/env python3

with open("data.txt") as file:
    lines = [line.rstrip() for line in file.readlines()]


def simple(lines=[]):
    dimensions = {}
    for item in lines:
        dimensions[item.split()[0]] = dimensions.get(item.split()[0], 0) + int(
            item.split()[1])

    print(dimensions)
    print((dimensions["down"] - dimensions["up"]) * dimensions["forward"])


def accurate(lines=[]):
    dimensions = {"horizontal": 0, "aim": 0, "depth": 0}

    for item in lines:
        if item.split()[0] == "down":
            dimensions["aim"] += int(item.split()[1])
        if item.split()[0] == "up":
            dimensions["aim"] -= int(item.split()[1])
        if item.split()[0] == "forward":
            dimensions["horizontal"] += int(item.split()[1])
            dimensions["depth"] += dimensions["aim"] * int(item.split()[1])

    print(dimensions)
    print(dimensions["horizontal"] * dimensions["depth"])


simple(lines)
accurate(lines)
