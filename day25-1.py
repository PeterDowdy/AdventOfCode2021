from itertools import *
import heapq
from collections import *
import ast
from typing import Any
import numpy as np

data = []
with open("day25.txt") as f:
    for x in f.readlines():
        data.append(x.strip())

cukes = {}
for y in range(0, len(data)):
    for x in range(0, len(data[y])):
        cukes[(x, y)] = data[y][x]

max_y = len(data)
max_x = len(data[0])

a_move_happened = True
move_count = 0
while a_move_happened:
    # buf = ""
    # for y in range(0, max_y):
    #     for x in range(0, max_x):
    #         buf += cukes[(x, y)]
    #     buf += "\n"
    move_count += 1
    print(f"Step {move_count}", end="\r")
    a_move_happened = False
    next_cukes = {}
    for k, v in cukes.items():
        if v != ">":
            continue
        next_step = (k[0] + 1, k[1])
        if next_step not in cukes:
            next_step = (0, next_step[1])
        if cukes[next_step] == ".":
            a_move_happened = True
            next_cukes[next_step] = ">"
            next_cukes[k] = "."
        else:
            next_cukes[k] = ">"
    cukes.update(next_cukes)
    next_cukes = {}
    for k, v in cukes.items():
        if v != "v":
            continue
        next_step = (k[0], k[1] + 1)
        if next_step not in cukes:
            next_step = (next_step[0], 0)
        if cukes[next_step] == ".":
            a_move_happened = True
            next_cukes[next_step] = "v"
            next_cukes[k] = "."
        else:
            next_cukes[k] = "v"
    cukes.update(next_cukes)
print()
print(move_count)
