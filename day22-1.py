from itertools import *
import heapq
from collections import *
import ast
from typing import Any
import numpy as np

data = []
with open("day22.txt") as f:
    for x in f.readlines():
        data.append(x.strip())

steps = []
for row in data:
    instruction = row.split(" ")[0]
    ranges = row.split(" ")[1].split(",")
    x_range = ranges[0].split("=")[1].split("..")
    y_range = ranges[1].split("=")[1].split("..")
    z_range = ranges[2].split("=")[1].split("..")
    x_min = int(x_range[0])
    x_max = int(x_range[1])
    y_min = int(y_range[0])
    y_max = int(y_range[1])
    z_min = int(z_range[0])
    z_max = int(z_range[1])
    steps.append((instruction, x_min, x_max, y_min, y_max, z_min, z_max))

cubes = {}

for step in steps[0:2]:
    instruction, x_min, x_max, y_min, y_max, z_min, z_max = step
    if x_min < -50 or x_max > 50:
        continue
    if y_min < -50 or y_max > 50:
        continue
    if z_min < -50 and z_max > 50:
        continue
    for x_range in range(x_min, x_max + 1):
        for y_range in range(y_min, y_max + 1):
            for z_range in range(z_min, z_max + 1):
                if instruction == "on":
                    cubes[(x_range, y_range, z_range)] = 1
                else:
                    cubes[(x_range, y_range, z_range)] = 0

print(len([x for x in cubes.values() if x == 1]))
