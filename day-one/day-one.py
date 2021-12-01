#!/usr/bin/env python3

with open("data.txt") as file:
    lines = [int(line.rstrip()) for line in file.readlines()]


def group(item_list=[]):
    grouped = [(i, sum(item_list[i:i + 3])) for i in range(1, len(item_list))
               if sum(item_list[i:i + 3]) > sum(item_list[i - 1:i + 2])]

    print(len(grouped))


def compare(item_list=[]):
    increased = [
        item_list[i] for i in range(1, len(item_list))
        if item_list[i] > item_list[i - 1]
    ]

    print(len(increased))


compare(lines)
group(lines)
