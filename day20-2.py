from itertools import *
import heapq
from collections import *
import ast
from typing import Any
import numpy as np

data = []
with open("day20.txt") as f:
    for x in f.readlines():
        data.append(x.strip())


infinity_value = "."


def add_margins(i):
    min_x = min(x[0] for x in i.keys())
    min_y = min(x[1] for x in i.keys())
    max_x = max(x[0] for x in i.keys())
    max_y = max(x[1] for x in i.keys())
    for x in range(min_x - 3, max_x + 3):
        for y in range(min_y - 3, max_y + 3):
            if (x, y) not in i:
                i[(x, y)] = infinity_value


def print_image(i):
    min_x = min(x[0] for x in i.keys())
    min_y = min(x[1] for x in i.keys())
    max_x = max(x[0] for x in i.keys())
    max_y = max(x[1] for x in i.keys())
    buf = ""
    for y in range(min_y, max_y + 1):
        for x in range(min_x, max_x + 1):
            buf += i[(x, y)]
        buf += "\n"
    print(buf)


iea = data[0]
image_rows = []
image = {}
for n in data[2:]:
    image_rows.append(list(n))

for y in range(0, len(image_rows)):
    for x in range(0, len(image_rows[0])):
        image[(x, y)] = image_rows[y][x]


for n in range(0, 50):
    add_margins(image)
    min_x = min(x[0] for x in image.keys())
    min_y = min(x[1] for x in image.keys())
    max_x = max(x[0] for x in image.keys())
    max_y = max(x[1] for x in image.keys())

    print(f"Processing {n}: ({min_x},{min_y} to {max_x},{max_y})", end="\r")

    next_image = {}
    for x in range(min_x + 1, max_x):
        for y in range(min_y + 1, max_y):
            key = (
                image[(x - 1, y - 1)]
                + image[(x, y - 1)]
                + image[(x + 1, y - 1)]
                + image[(x - 1, y)]
                + image[(x, y)]
                + image[(x + 1, y)]
                + image[(x - 1, y + 1)]
                + image[(x, y + 1)]
                + image[(x + 1, y + 1)]
            )

            binary = int(key.replace("#", "1").replace(".", "0"), 2)
            next_image[(x, y)] = iea[binary]
    image = next_image
    if iea[0] == "#" and iea[-1] == ".":
        infinity_value = "#" if infinity_value == "." else "."
print()
print(sum(1 if x == "#" else 0 for x in image.values()))
