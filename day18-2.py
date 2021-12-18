from itertools import *
import heapq
from collections import *
import ast
from typing import Any

data = []
with open("day18.txt") as f:
    for x in f.readlines():
        data.append(x.strip())


class Node:
    def __init__(self, record, parent, depth):
        self.parent = parent
        self.depth = depth
        self.value = None
        self.left = None
        self.right = None
        if isinstance(record, int):
            self.value = record
        else:
            self.left = Node(record[0], self, self.depth + 1)
            self.right = Node(record[1], self, self.depth + 1)


data = [ast.literal_eval(x) for x in data]


def find_left_value(last_left, tree):
    if tree is None:
        return None
    if tree.left == last_left:
        return find_left_value(tree, tree.parent)
    search = tree.left
    while search.right is not None:
        search = search.right
    return search


def find_right_val(last_right, tree):
    if tree is None:
        return None
    if tree.right == last_right:
        return find_right_val(tree, tree.parent)
    search = tree.right
    while search.left is not None:
        search = search.left
    return search


def explode(tree):
    left_val = find_left_value(tree, tree.parent)
    right_val = find_right_val(tree, tree.parent)
    if left_val is not None:
        left_val.value += tree.left.value
    if right_val is not None:
        right_val.value += tree.right.value
    tree.value = 0
    tree.left = None
    tree.right = None


def split(tree):
    tree.left = Node(tree.value // 2, tree, tree.depth + 1)
    tree.right = Node(tree.value // 2 + tree.value % 2, tree, tree.depth + 1)
    tree.value = None


def recurse(tree: Node, ops: list):
    if (
        tree.left is not None
        and tree.left.value is not None
        and tree.right is not None
        and tree.right.value is not None
        and tree.depth >= 4
    ):
        ops.append(("explode", tree))
    elif tree.value is not None and tree.value >= 10:
        ops.append(("split", tree))
    else:
        if tree.left is not None:
            recurse(tree.left, ops)
        if tree.right is not None:
            recurse(tree.right, ops)
    return tree


def print_tree(tree):
    if tree.value is not None:
        return str(tree.value)
    else:
        return "[" + print_tree(tree.left) + ", " + print_tree(tree.right) + "]"


def sum_tree(tree):
    if tree.value is not None:
        return tree.value
    else:
        return 3 * sum_tree(tree.left) + 2 * sum_tree(tree.right)


largest = 0
step = 0
total = len(data) * len(data)
for x in data:
    for y in data:
        step += 1
        print(f"step {step} of {total}", end="\r")
        if x == y:
            continue
        r_tree = Node([x, y], None, 0)
        while True:
            ops = []
            recurse(r_tree, ops)
            if len(ops) == 0:
                break
            elif any(x[0] == "explode" for x in ops):
                explode(next(x[1] for x in ops if x[0] == "explode"))
            elif any(x[0] == "split" for x in ops):
                split(next(x[1] for x in ops if x[0] == "split"))
        prev_tree = r_tree
        largest = max(largest, sum_tree(r_tree))
print()
print(largest)
