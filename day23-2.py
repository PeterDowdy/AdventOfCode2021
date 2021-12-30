from itertools import *
import heapq
from collections import *
import ast
from typing import Any
import numpy as np

positions = {
    ("alcove", 0, 0): "D",
    ("alcove", 0, 1): "D",
    ("alcove", 0, 2): "D",
    ("alcove", 0, 3): "B",
    ("alcove", 1, 0): "A",
    ("alcove", 1, 1): "C",
    ("alcove", 1, 2): "B",
    ("alcove", 1, 3): "C",
    ("alcove", 2, 0): "C",
    ("alcove", 2, 1): "B",
    ("alcove", 2, 2): "A",
    ("alcove", 2, 3): "B",
    ("alcove", 3, 0): "D",
    ("alcove", 3, 1): "A",
    ("alcove", 3, 2): "C",
    ("alcove", 3, 3): "A",
    ("hallway", 0): ".",
    ("hallway", 1): ".",
    ("hallway", 2): ".",
    ("hallway", 3): ".",
    ("hallway", 4): ".",
    ("hallway", 5): ".",
    ("hallway", 6): ".",
    ("hallway", 7): ".",
    ("hallway", 8): ".",
    ("hallway", 9): ".",
    ("hallway", 10): ".",
}

test_positions = {
    ("alcove", 0, 0): "B",
    ("alcove", 0, 1): "D",
    ("alcove", 0, 2): "D",
    ("alcove", 0, 3): "A",
    ("alcove", 1, 0): "C",
    ("alcove", 1, 1): "C",
    ("alcove", 1, 2): "B",
    ("alcove", 1, 3): "D",
    ("alcove", 2, 0): "B",
    ("alcove", 2, 1): "B",
    ("alcove", 2, 2): "A",
    ("alcove", 2, 3): "C",
    ("alcove", 3, 0): "D",
    ("alcove", 3, 1): "A",
    ("alcove", 3, 2): "C",
    ("alcove", 3, 3): "A",
    ("hallway", 0): ".",
    ("hallway", 1): ".",
    ("hallway", 2): ".",
    ("hallway", 3): ".",
    ("hallway", 4): ".",
    ("hallway", 5): ".",
    ("hallway", 6): ".",
    ("hallway", 7): ".",
    ("hallway", 8): ".",
    ("hallway", 9): ".",
    ("hallway", 10): ".",
}

# positions = test_positions

move_costs = {"A": 1, "B": 10, "C": 100, "D": 1000}


def dump_map(map):
    return f"""#############
#{map[("hallway",0)]}{map[("hallway",1)]}{map[("hallway",2)]}{map[("hallway",3)]}{map[("hallway",4)]}{map[("hallway",5)]}{map[("hallway",6)]}{map[("hallway",7)]}{map[("hallway",8)]}{map[("hallway",9)]}{map[("hallway",10)]}#
###{map[("alcove",0,0)]}#{map[("alcove",1,0)]}#{map[("alcove",2,0)]}#{map[("alcove",3,0)]}###
  #{map[("alcove",0,1)]}#{map[("alcove",1,1)]}#{map[("alcove",2,1)]}#{map[("alcove",3,1)]}#
  #{map[("alcove",0,2)]}#{map[("alcove",1,2)]}#{map[("alcove",2,2)]}#{map[("alcove",3,2)]}#
  #{map[("alcove",0,3)]}#{map[("alcove",1,3)]}#{map[("alcove",2,3)]}#{map[("alcove",3,3)]}#
  #########"""


def can_reach_hallway_from_alcove(alcove, hallway, map):
    end = hallway[1]
    if end in [2, 4, 6, 8]:
        return (False, 0)
    if alcove[1] == 0:
        start = 2
    elif alcove[1] == 1:
        start = 4
    elif alcove[1] == 2:
        start = 6
    elif alcove[1] == 3:
        start = 8
    total_cost_so_far = 1 + alcove[2]
    current = start
    while current != end:
        current += -1 if start > end else 1
        if map[("hallway", current)] == ".":
            total_cost_so_far += 1
        else:
            return (False, 0)
    return (True, total_cost_so_far)


def can_reach_alcove_from_hallway(hallway, alcove, map):
    start = hallway[1]
    if alcove[1] == 0:
        end = 2
    elif alcove[1] == 1:
        end = 4
    elif alcove[1] == 2:
        end = 6
    elif alcove[1] == 3:
        end = 8
    total_cost_so_far = 1 + alcove[2]
    current = start
    while current != end:
        current += -1 if start > end else 1
        if map[("hallway", current)] == ".":
            total_cost_so_far += 1
        else:
            return (False, 0)
    return (True, total_cost_so_far)


def can_reach(start, end, map):
    if map[end] != ".":
        return (False, 0)
    if start[0] == ("alcove"):
        if start[2] == 1:
            if map[(start[0], start[1], 0)] != ".":
                return (False, 0)
        if start[2] == 2:
            if map[(start[0], start[1], 1)] != ".":
                return (False, 0)
        if start[2] == 3:
            if map[(start[0], start[1], 2)] != ".":
                return (False, 0)
        if end[0] == "hallway":
            if end[1] in [2, 4, 6, 8]:
                return (False, 0)
            you_can, cost = can_reach_hallway_from_alcove(start, end, map)
            return (
                you_can,
                cost,
            )
        elif end[0] == "alcove":
            if end[1] == start[1]:
                return (False, 0)
            if end[2] == 0 and map[(end[0], end[1], 1)] == ".":
                return (False, 0)
            if end[2] == 1 and map[(end[0], end[1], 2)] == ".":
                return (False, 0)
            if end[2] == 2 and map[(end[0], end[1], 3)] == ".":
                return (False, 0)

            alcove_members = [
                map[("alcove", end[1], x)]
                for x in range(0, 4)
                if map[("alcove", end[1], x)] != "."
            ]
            if any(x != map[start] for x in alcove_members):
                return (False, 0)
            if start[1] == 0:
                hallway_intersection = 2
            elif start[1] == 1:
                hallway_intersection = 4
            elif start[1] == 2:
                hallway_intersection = 6
            elif start[1] == 3:
                hallway_intersection = 8
            you_can, cost = can_reach_alcove_from_hallway(
                ("hallway", hallway_intersection), end, map
            )
            return (you_can, cost + 1 + start[2])
    if start[0] == "hallway":
        if end[0] == "hallway":
            return (False, 0)
        elif end[0] == "alcove":
            if end[2] == 0 and map[(end[0], end[1], 1)] == ".":
                return (False, 0)
            if end[2] == 1 and map[(end[0], end[1], 2)] == ".":
                return (False, 0)
            if end[2] == 2 and map[(end[0], end[1], 3)] == ".":
                return (False, 0)
            alcove_members = [
                map[("alcove", end[1], x)]
                for x in range(0, 4)
                if map[("alcove", end[1], x)] != "."
            ]
            if any(x != map[start] for x in alcove_members):
                return (False, 0)
            you_can, cost = can_reach_alcove_from_hallway(start, end, map)
            return (you_can, cost)


def win(map):
    return (
        map[("alcove", 0, 0)] == map[("alcove", 0, 1)]
        and map[("alcove", 0, 0)] == map[("alcove", 0, 2)]
        and map[("alcove", 0, 0)] == map[("alcove", 0, 3)]
        and map[("alcove", 0, 0)] == "A"
        and map[("alcove", 1, 0)] == map[("alcove", 1, 1)]
        and map[("alcove", 1, 0)] == map[("alcove", 1, 2)]
        and map[("alcove", 1, 0)] == map[("alcove", 1, 3)]
        and map[("alcove", 1, 0)] == "B"
        and map[("alcove", 2, 0)] == map[("alcove", 2, 1)]
        and map[("alcove", 2, 0)] == map[("alcove", 2, 2)]
        and map[("alcove", 2, 0)] == map[("alcove", 2, 3)]
        and map[("alcove", 2, 0)] == "C"
        and map[("alcove", 3, 0)] == map[("alcove", 3, 1)]
        and map[("alcove", 3, 0)] == map[("alcove", 3, 2)]
        and map[("alcove", 3, 0)] == map[("alcove", 3, 3)]
        and map[("alcove", 3, 0)] == "D"
    )


def is_in_the_right_place(start, amphi, current_best_map):
    if start[0] != "alcove":
        return False
    if amphi == "A" and start[1] != 0:
        return False
    if amphi == "B" and start[1] != 1:
        return False
    if amphi == "C" and start[1] != 2:
        return False
    if amphi == "D" and start[1] != 3:
        return False

    alcove_members = [
        current_best_map[("alcove", start[1], x)]
        for x in range(0, 4)
        if current_best_map[("alcove", start[1], x)] != "."
    ]
    if any(x != amphi for x in alcove_members):
        return False
    return True


seen_maps = {}
solutions = [(0, 0, {k: v for k, v in positions.items()}, [dump_map(positions)])]
iteration = 0
ctr = 0
while len(solutions) > 0:
    iteration += 1
    current_best_cost, _, current_best_map, move_history = heapq.heappop(solutions)
    if iteration % 10000 == 0:
        seen_maps = {k: v for k, v in seen_maps.items() if v >= current_best_cost / 2}
    if (
        dump_map(current_best_map) in seen_maps
        and current_best_cost > seen_maps[dump_map(current_best_map)]
    ):
        continue
    print(
        f"Iteration {iteration}... testing route with cost {current_best_cost}.",
        end="\r",
    )
    if win(current_best_map):
        print()
        print(dump_map(current_best_map))
        print("You win!")
        print(current_best_cost)
        break
    next_solutions = []
    for start, amphi in current_best_map.items():
        if amphi == ".":
            continue
        for end in current_best_map.keys():
            if end == start:
                continue
            if amphi == "A" and end[0] == "alcove" and end[1] != 0:
                continue
            if amphi == "B" and end[0] == "alcove" and end[1] != 1:
                continue
            if amphi == "C" and end[0] == "alcove" and end[1] != 2:
                continue
            if amphi == "D" and end[0] == "alcove" and end[1] != 3:
                continue
            if is_in_the_right_place(start, amphi, current_best_map):
                continue
            you_can, steps = can_reach(start, end, current_best_map)
            if you_can:
                next_map = {k: v for k, v in current_best_map.items()}
                next_map[end] = current_best_map[start]
                next_map[start] = "."
                next_cost = current_best_cost + steps * move_costs[amphi]
                if (
                    dump_map(next_map) in seen_maps
                    and next_cost >= seen_maps[dump_map(next_map)]
                ):
                    continue
                heapq.heappush(
                    solutions,
                    (next_cost, ctr, next_map, move_history + [dump_map(next_map)]),
                )
                ctr += 1
                seen_maps[dump_map(next_map)] = next_cost
