from itertools import *
import heapq
from collections import *
import ast
from typing import Any
import numpy as np

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.colors as mcolors

fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")
should_draw = False
should_compare = False

data = []
with open("day22.txt") as f:
    for x in f.readlines():
        data.append(x.strip())

steps = []
ctr = 0
for row in data:
    instruction = row.split(" ")[0]
    ranges = row.split(" ")[1].split(",")
    x_range = ranges[0].split("=")[1].split("..")
    y_range = ranges[1].split("=")[1].split("..")
    z_range = ranges[2].split("=")[1].split("..")
    x_min = int(x_range[0])
    x_max = int(x_range[1]) + 1
    y_min = int(y_range[0])
    y_max = int(y_range[1]) + 1
    z_min = int(z_range[0])
    z_max = int(z_range[1]) + 1
    steps.append((ctr, instruction, x_min, x_max, y_min, y_max, z_min, z_max))
    ctr += 1

cubes = {}


def find_overlap(inner_step, outer_step):
    while len(inner_step) < 8:
        inner_step = (None,) + inner_step
    while len(outer_step) < 8:
        outer_step = (None,) + outer_step
    (
        _,
        _,
        outer_x_min,
        outer_x_max,
        outer_y_min,
        outer_y_max,
        outer_z_min,
        outer_z_max,
    ) = outer_step

    (
        _,
        _,
        inner_x_min,
        inner_x_max,
        inner_y_min,
        inner_y_max,
        inner_z_min,
        inner_z_max,
    ) = inner_step
    return not (
        inner_x_max <= outer_x_min
        or outer_x_max <= inner_x_min
        or inner_z_max <= outer_z_min
        or outer_z_max <= inner_z_min
        or inner_y_max <= outer_y_min
        or outer_y_max <= inner_y_min
    )


def get_area(area):
    while len(area) < 8:
        area = (None,) + area
    (_, _, x_min, x_max, y_min, y_max, z_min, z_max) = area
    return (abs(x_max - x_min)) * (abs(y_max - y_min)) * (abs(z_max - z_min))


def get_overlaps(row, region):
    while len(row) < 8:
        row = (None,) + row
    while len(region) < 8:
        region = (None,) + region
    (_, _, x_min, x_max, y_min, y_max, z_min, z_max) = row
    (
        _,
        _,
        overlap_x_min,
        overlap_x_max,
        overlap_y_min,
        overlap_y_max,
        overlap_z_min,
        overlap_z_max,
    ) = region
    return [
        (  # (0,0,0)
            min(x_min, overlap_x_min),
            max(x_min, overlap_x_min),
            min(y_min, overlap_y_min),
            max(y_min, overlap_y_min),
            min(z_min, overlap_z_min),
            max(z_min, overlap_z_min),
        ),
        (  # (0,0,1)
            min(x_min, overlap_x_min),
            max(x_min, overlap_x_min),
            min(y_min, overlap_y_min),
            max(y_min, overlap_y_min),
            max(z_min, overlap_z_min),
            min(z_max, overlap_z_max),
        ),
        (  # (0,0,2)
            min(x_min, overlap_x_min),
            max(x_min, overlap_x_min),
            min(y_min, overlap_y_min),
            max(y_min, overlap_y_min),
            min(z_max, overlap_z_max),
            max(z_max, overlap_z_max),
        ),
        (  # (0,1,0)
            min(x_min, overlap_x_min),
            max(x_min, overlap_x_min),
            max(y_min, overlap_y_min),
            min(y_max, overlap_y_max),
            min(z_min, overlap_z_min),
            max(z_min, overlap_z_min),
        ),
        (  # (0,1,1)
            min(x_min, overlap_x_min),
            max(x_min, overlap_x_min),
            max(y_min, overlap_y_min),
            min(y_max, overlap_y_max),
            max(z_min, overlap_z_min),
            min(z_max, overlap_z_max),
        ),
        (  # (0,1,2)
            min(x_min, overlap_x_min),
            max(x_min, overlap_x_min),
            max(y_min, overlap_y_min),
            min(y_max, overlap_y_max),
            min(z_max, overlap_z_max),
            max(z_max, overlap_z_max),
        ),
        (  # (0,2,0)
            min(x_min, overlap_x_min),
            max(x_min, overlap_x_min),
            min(y_max, overlap_y_max),
            max(y_max, overlap_y_max),
            min(z_min, overlap_z_min),
            max(z_min, overlap_z_min),
        ),
        (  # (0,2,1)
            min(x_min, overlap_x_min),
            max(x_min, overlap_x_min),
            min(y_max, overlap_y_max),
            max(y_max, overlap_y_max),
            max(z_min, overlap_z_min),
            min(z_max, overlap_z_max),
        ),
        (  # (0,2,2)
            min(x_min, overlap_x_min),
            max(x_min, overlap_x_min),
            min(y_max, overlap_y_max),
            max(y_max, overlap_y_max),
            min(z_max, overlap_z_max),
            max(z_max, overlap_z_max),
        ),
        (  # (1,0,0)
            max(x_min, overlap_x_min),
            min(x_max, overlap_x_max),
            min(y_min, overlap_y_min),
            max(y_min, overlap_y_min),
            min(z_min, overlap_z_min),
            max(z_min, overlap_z_min),
        ),
        (  # (1,0,1)
            max(x_min, overlap_x_min),
            min(x_max, overlap_x_max),
            min(y_min, overlap_y_min),
            max(y_min, overlap_y_min),
            max(z_min, overlap_z_min),
            min(z_max, overlap_z_max),
        ),
        (  # (1,0,2)
            max(x_min, overlap_x_min),
            min(x_max, overlap_x_max),
            min(y_min, overlap_y_min),
            max(y_min, overlap_y_min),
            min(z_max, overlap_z_max),
            max(z_max, overlap_z_max),
        ),
        (  # (1,1,0)
            max(x_min, overlap_x_min),
            min(x_max, overlap_x_max),
            max(y_min, overlap_y_min),
            min(y_max, overlap_y_max),
            min(z_min, overlap_z_min),
            max(z_min, overlap_z_min),
        ),
        (  # (1,1,1)
            max(x_min, overlap_x_min),
            min(x_max, overlap_x_max),
            max(y_min, overlap_y_min),
            min(y_max, overlap_y_max),
            max(z_min, overlap_z_min),
            min(z_max, overlap_z_max),
        ),
        (  # (1,1,2)
            max(x_min, overlap_x_min),
            min(x_max, overlap_x_max),
            max(y_min, overlap_y_min),
            min(y_max, overlap_y_max),
            min(z_max, overlap_z_max),
            max(z_max, overlap_z_max),
        ),
        (  # (1,2,0)
            max(x_min, overlap_x_min),
            min(x_max, overlap_x_max),
            min(y_max, overlap_y_max),
            max(y_max, overlap_y_max),
            min(z_min, overlap_z_min),
            max(z_min, overlap_z_min),
        ),
        (  # (1,2,1)
            max(x_min, overlap_x_min),
            min(x_max, overlap_x_max),
            min(y_max, overlap_y_max),
            max(y_max, overlap_y_max),
            max(z_min, overlap_z_min),
            min(z_max, overlap_z_max),
        ),
        (  # (1,2,2)
            max(x_min, overlap_x_min),
            min(x_max, overlap_x_max),
            min(y_max, overlap_y_max),
            max(y_max, overlap_y_max),
            min(z_max, overlap_z_max),
            max(z_max, overlap_z_max),
        ),
        (  # (2,0,0)
            min(x_max, overlap_x_max),
            max(x_max, overlap_x_max),
            min(y_min, overlap_y_min),
            max(y_min, overlap_y_min),
            min(z_min, overlap_z_min),
            max(z_min, overlap_z_min),
        ),
        (  # (2,0,1)
            min(x_max, overlap_x_max),
            max(x_max, overlap_x_max),
            min(y_min, overlap_y_min),
            max(y_min, overlap_y_min),
            max(z_min, overlap_z_min),
            min(z_max, overlap_z_max),
        ),
        (  # (2,0,2)
            min(x_max, overlap_x_max),
            max(x_max, overlap_x_max),
            min(y_min, overlap_y_min),
            max(y_min, overlap_y_min),
            min(z_max, overlap_z_max),
            max(z_max, overlap_z_max),
        ),
        (  # (2,1,0)
            min(x_max, overlap_x_max),
            max(x_max, overlap_x_max),
            max(y_min, overlap_y_min),
            min(y_max, overlap_y_max),
            min(z_min, overlap_z_min),
            max(z_min, overlap_z_min),
        ),
        (  # (2,1,1)
            min(x_max, overlap_x_max),
            max(x_max, overlap_x_max),
            max(y_min, overlap_y_min),
            min(y_max, overlap_y_max),
            max(z_min, overlap_z_min),
            min(z_max, overlap_z_max),
        ),
        (  # (2,1,2)
            min(x_max, overlap_x_max),
            max(x_max, overlap_x_max),
            max(y_min, overlap_y_min),
            min(y_max, overlap_y_max),
            min(z_max, overlap_z_max),
            max(z_max, overlap_z_max),
        ),
        (  # (2,2,0)
            min(x_max, overlap_x_max),
            max(x_max, overlap_x_max),
            min(y_max, overlap_y_max),
            max(y_max, overlap_y_max),
            min(z_min, overlap_z_min),
            max(z_min, overlap_z_min),
        ),
        (  # (2,2,1)
            min(x_max, overlap_x_max),
            max(x_max, overlap_x_max),
            min(y_max, overlap_y_max),
            max(y_max, overlap_y_max),
            max(z_min, overlap_z_min),
            min(z_max, overlap_z_max),
        ),
        (  # (2,2,2)
            min(x_max, overlap_x_max),
            max(x_max, overlap_x_max),
            min(y_max, overlap_y_max),
            max(y_max, overlap_y_max),
            min(z_max, overlap_z_max),
            max(z_max, overlap_z_max),
        ),
    ]


def draw_cubes(*cubes):
    colors = iter(v for v in mcolors.XKCD_COLORS.values())
    for row in cubes:
        while len(row) < 8:
            row = (None,) + row
        (_, _, x_min, x_max, y_min, y_max, z_min, z_max) = row
        course = [
            # face
            (x_min, y_min, z_min),
            (x_max, y_min, z_min),
            (x_max, y_min, z_max),
            (x_min, y_min, z_max),
            (x_min, y_min, z_min),
            # face
            (x_min, y_max, z_min),
            (x_min, y_max, z_max),
            (x_min, y_min, z_max),
            (x_min, y_min, z_min),
            # face
            (x_max, y_min, z_min),
            (x_max, y_max, z_min),
            (x_min, y_max, z_min),
            (x_min, y_min, z_min),
            # move
            (x_min, y_min, z_max),
            # face
            (x_max, y_min, z_max),
            (x_max, y_max, z_max),
            (x_min, y_max, z_max),
            # face
            (x_max, y_max, z_max),
            (x_max, y_max, z_min),
            # face
            (x_max, y_min, z_min),
        ]
        ax.plot3D(
            xs=[x for x, y, z in course],
            ys=[y for x, y, z in course],
            zs=[z for x, y, z in course],
            color=next(colors),
        )
    plt.show(block=False)


def consolidate_regions(regions):
    still_consolidating = True
    while still_consolidating:
        next_regions = {}
        still_consolidating = False
        purge_regions = []
        sorted_regions = list(sorted(regions.items(), key=lambda kvp: -1 * kvp[1][0]))
        for k_1, v_1 in sorted_regions:
            for k_2, v_2 in sorted_regions:
                if k_1 == k_2:
                    continue
                if k_1 in purge_regions or k_2 in purge_regions:
                    continue
                (
                    outer_x_min,
                    outer_x_max,
                    outer_y_min,
                    outer_y_max,
                    outer_z_min,
                    outer_z_max,
                ) = k_1

                (
                    inner_x_min,
                    inner_x_max,
                    inner_y_min,
                    inner_y_max,
                    inner_z_min,
                    inner_z_max,
                ) = k_2
                combined_x_min = min(outer_x_min, inner_x_min)
                combined_x_max = max(outer_x_max, inner_x_max)
                combined_y_min = min(outer_y_min, inner_y_min)
                combined_y_max = max(outer_y_max, inner_y_max)
                combined_z_min = min(outer_z_min, inner_z_min)
                combined_z_max = max(outer_z_max, inner_z_max)
                if (get_area(k_1) + get_area(k_2)) == get_area(
                    (
                        combined_x_min,
                        combined_x_max,
                        combined_y_min,
                        combined_y_max,
                        combined_z_min,
                        combined_z_max,
                    )
                ):
                    still_consolidating = True
                    next_regions[
                        (
                            combined_x_min,
                            combined_x_max,
                            combined_y_min,
                            combined_y_max,
                            combined_z_min,
                            combined_z_max,
                        )
                    ] = (max(v_1[0], v_2[0]), v_1[1] if v_1[0] > v_2[0] else v_2[1])
                    purge_regions += [k_1, k_2]
        next_regions.update(
            {k: v for k, v in regions.items() if k not in purge_regions}
        )
        regions = next_regions
    return regions


# enveloped_steps = []
# for step_1 in steps:
#     for step_2 in steps:
#         if step_1 == step_2:
#             continue
#         (_, _, x_min1, x_max1, y_min1, y_max1, z_min1, z_max1) = step_1
#         (_, _, x_min2, x_max2, y_min2, y_max2, z_min2, z_max2) = step_2
#         if (
#             x_min1 >= x_min2
#             and x_max1 <= x_max2
#             and y_min1 >= y_min2
#             and y_max1 <= y_max2
#             and z_min1 >= z_min2
#             and z_max1 <= z_max2
#         ):
#             enveloped_steps.append(step_1)

# steps = [x for x in steps if x not in enveloped_steps]


regions = {}
step_ctr = 0
ops = 0
for row in steps:
    step_ctr += 1
    new_regions = {}
    if should_draw:
        plt.cla()
        draw_cubes(*[k for k in regions.keys()])
    overlap_regions = []
    a_change_happened = False
    regions_to_process = [k for k in regions.keys()]
    print(
        f"({step_ctr}/{len(steps)}) number of regions: {len(regions)}, ops:{ops}",
        end="\r",
    )
    (ix, instruction, x_min, x_max, y_min, y_max, z_min, z_max) = row
    region_1 = tuple(list(row)[2:])
    next_regions = {region_1: (ix, instruction)}
    for region_2 in regions_to_process:
        ops += 1
        if find_overlap(
            region_1,
            region_2,
        ):
            overlap_regions = [region_1, region_2]
            if should_draw:
                plt.cla()
                cubes_to_draw = [region_1, region_2]
                draw_cubes(*cubes_to_draw)
            descendants = get_overlaps(region_1, region_2)
            if should_draw:
                plt.cla()
                draw_cubes(*descendants)
            for d in set(descendants):
                d_x_min, d_x_max, d_y_min, d_y_max, d_z_min, d_z_max = d
                if d_x_min == d_x_max or d_y_min == d_y_max or d_z_min == d_z_max:
                    continue
                if not find_overlap(region_1, d) and find_overlap(region_2, d):
                    ix, instruction = regions[region_2]
                    next_regions[d] = (ix, instruction)
                    if should_draw:
                        cubes_to_draw += [d]
                        plt.cla()
                        draw_cubes(*cubes_to_draw)
                    pass
            if should_draw:
                plt.cla()
                draw_cubes(*cubes_to_draw)
            pass
        else:
            next_regions[region_2] = regions[region_2]
    regions = next_regions
print()
part2_cubes_area = 0

for k, v in regions.items():
    if v[1] == "on":
        part2_cubes_area += get_area(k)
print(part2_cubes_area)

if should_compare:
    for step, v in regions.items():
        x_min, x_max, y_min, y_max, z_min, z_max = step
        instruction = v[1]
        x_ctr = 0
        before = len(cubes)
        for x_range in range(x_min, x_max):
            x_ctr += 1
            y_ctr = 0
            for y_range in range(y_min, y_max):
                z_ctr = 0
                y_ctr += 1
                for z_range in range(z_min, z_max):
                    z_ctr += 1
                    if instruction == "on":
                        cubes[(x_range, y_range, z_range)] = 1
                    else:
                        cubes[(x_range, y_range, z_range)] = 0
        after = len(cubes)

    print(sum([x for x in cubes.values()]))

    their_cubes = {}

    for step in steps:
        _, instruction, x_min, x_max, y_min, y_max, z_min, z_max = step
        if x_min < -50 or x_max > 50:
            continue
        if y_min < -50 or y_max > 50:
            continue
        if z_min < -50 and z_max > 50:
            continue
        for x_range in range(x_min, x_max):
            for y_range in range(y_min, y_max):
                for z_range in range(z_min, z_max):
                    if instruction == "on":
                        their_cubes[(x_range, y_range, z_range)] = 1
                    else:
                        their_cubes[(x_range, y_range, z_range)] = 0

    print(sum([x for x in their_cubes.values()]))

    diff = list(set(their_cubes.keys()).difference(set(cubes.keys())))

    if len(diff) > 0:
        min_x = min(x for x, y, z in diff)
        max_x = max(x for x, y, z in diff)
        min_y = min(y for x, y, z in diff)
        max_y = max(y for x, y, z in diff)
        min_z = min(z for x, y, z in diff)
        max_z = max(z for x, y, z in diff)
        plt.cla()
        draw_cubes(*[k for k in regions.keys()])
        ax.scatter(
            xs=[x for x, y, z in diff],
            ys=[y for x, y, z in diff],
            zs=[z for x, y, z in diff],
        )
    pass
