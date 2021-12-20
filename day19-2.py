from itertools import *
import heapq
from collections import *
import ast
from typing import Any
import numpy as np

data = []
with open("day19.txt") as f:
    for x in f.readlines():
        data.append(x.strip())

scanners = {}
scanner_positions = {0: (0, 0, 0)}
scanner_number = ""

rotate_x = [[1, 0, 0], [0, 0, -1], [0, 1, 0]]
rotate_y = [[0, 0, 1], [0, 1, 0], [-1, 0, 0]]
rotate_z = [[0, -1, 0], [1, 0, 0], [0, 0, 1]]

seen = []
rotations = []
for x in range(0, 4):
    for y in range(0, 4):
        for z in range(0, 4):
            rot_buf = np.identity(3)
            for n in range(0, x):
                rot_buf = np.matmul(rot_buf, rotate_x)
            for n in range(0, y):
                rot_buf = np.matmul(rot_buf, rotate_y)
            for n in range(0, z):
                rot_buf = np.matmul(rot_buf, rotate_z)
            rotuple = tuple([tuple(x) for x in rot_buf])
            if rotuple in seen:
                continue
            rotations.append(rot_buf)
            seen.append(rotuple)


def find_overlap_candidates(scanner_one, scanner_two, rotation=np.identity(3)):
    vec_diff = find_vec_diff(scanner_one, [np.matmul(x, rotation) for x in scanner_two])
    if vec_diff is not None:
        return (True, vec_diff)
    return (False, None)


def find_vec_diff(s_1, s_2):
    vec_diff = Counter()
    for b_one in s_1:
        for b_two in s_2:
            vec_diff[
                (
                    int(b_one[0] - b_two[0]),
                    int(b_one[1] - b_two[1]),
                    int(b_one[2] - b_two[2]),
                )
            ] += 1
    # print(max(x for x in vec_diff.values()))
    print("", end="")
    if any(x >= 12 for x in vec_diff.values()):
        translation = next(k for k, v in vec_diff.items() if v >= 12)
        return translation


for x in data:
    if "---" in x:
        scanner_number = int(x.replace("--- scanner ", "").replace(" ---", ""))
        scanners[scanner_number] = []
    elif len(x) > 0:
        scanners[scanner_number].append(ast.literal_eval(f"[{x}]"))

known_list = [0]


while len(known_list) < len(scanners.keys()):
    search_space = [s for s in scanners.keys() if s not in known_list]
    found = False
    for k in known_list:
        for s in search_space:
            for r in rotations:
                found_overlap, vec_diff = find_overlap_candidates(
                    scanners[k], scanners[s], r
                )
                if found_overlap:
                    print(f"reorienting {s} according to {k} using {r}")
                    scanners[s] = (np.matmul(scanners[s], r) + vec_diff).tolist()
                    scanner_positions[s] = vec_diff
                    known_list.append(s)
                    found = True
                if found:
                    break
            if found:
                break
        if found:
            break

beacons = set(map(tuple, scanners[0]))
for s in scanners.keys():
    if s == 0:
        continue
    beacons = beacons.union(set(map(tuple, scanners[s])))

beacons = list(beacons)


def manhattan_distance(coord1, coord2):
    return (
        abs(coord1[0] - coord2[0])
        + abs(coord1[1] - coord2[1])
        + abs(coord1[2] - coord2[2])
    )


farthest_distance = 0
for scanner_one in scanner_positions.values():
    for scanner_two in scanner_positions.values():
        md = manhattan_distance(scanner_one, scanner_two)
        if md > farthest_distance:
            farthest_distance = md

print(farthest_distance)
