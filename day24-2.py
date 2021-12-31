from itertools import *
import heapq
from collections import *
import ast
from typing import Any
import numpy as np

data = []
with open("day24.txt") as f:
    for x in f.readlines():
        data.append(x.strip())
sub_programs = []
current_program = []

for instr in data:
    if instr[0:3] == "inp" and len(current_program) > 0:
        sub_programs.append(current_program)
        current_program = [instr]
    else:
        current_program.append(instr)

sub_programs.append(current_program)


def execute_program(instructions, test_number, registers=None):
    registers = registers or {"w": 0, "x": 0, "y": 0, "z": 0}

    def parse_clause(b):
        if b.lstrip("-").isnumeric():
            return int(b)
        return int(registers[b])

    input = iter(str(test_number))

    def inp(a):
        registers[a] = next(input)

    def add(a, b):
        registers[a] += parse_clause(b)

    def mul(a, b):
        registers[a] *= parse_clause(b)

    def div(a, b):
        registers[a] //= parse_clause(b)

    def mod(a, b):
        registers[a] %= parse_clause(b)

    def eql(a, b):
        if registers[a] == parse_clause(b):
            registers[a] = 1
        else:
            registers[a] = 0

    for instr in instructions:
        toks = instr.split(" ")
        locals()[toks[0]](*toks[1:])

    return registers


test_number = "11111111111111"

first_five_subprogram = (
    sub_programs[0]
    + sub_programs[1]
    + sub_programs[2]
    + sub_programs[3]
    + sub_programs[4]
)

six_seven_subprogram = sub_programs[5] + sub_programs[6]

eight_nine_ten_subprogram = sub_programs[7] + sub_programs[8] + sub_programs[9]


def increment(n):
    n = int(n) + 1
    return str(n).replace("0", "1")


invalids = {k: [] for k in range(0, 14)}


def get_valid_sequence(start, end, z=0):
    if z in invalids[start]:
        return
    term = test_number[start : end + 1]
    sub_program_sequence = []
    for n in range(start, end + 1):
        sub_program_sequence += sub_programs[n]
    any_found = False
    while int(term) <= int("".join((1 + end - start) * ["9"])):
        registers = execute_program(
            sub_program_sequence, term, {"w": 0, "x": 0, "y": 0, "z": z}
        )
        if registers["x"] == 0:
            any_found = True
            yield (term, registers["z"])
        term = increment(term)
    if not any_found:
        invalids[start].append(z)


for first_five, z in get_valid_sequence(0, 4):
    print(first_five + "??" + "???" + "?" + "?" + "?" + "?", end="\r")
    for six_seven, z in get_valid_sequence(5, 6, z):
        print(first_five + six_seven + "???" + "?" + "?" + "?" + "?", end="\r")
        for eight_nine_ten, z in get_valid_sequence(7, 9, z):
            print(
                first_five + six_seven + eight_nine_ten + "?" + "?" + "?" + "?",
                end="\r",
            )
            for eleven, z in get_valid_sequence(10, 10, z):
                print(
                    first_five + six_seven + eight_nine_ten + eleven + "?" + "?" + "?",
                    end="\r",
                )
                for twelve, z in get_valid_sequence(11, 11, z):
                    print(
                        first_five
                        + six_seven
                        + eight_nine_ten
                        + eleven
                        + twelve
                        + "?"
                        + "?",
                        end="\r",
                    )
                    for thirteen, z in get_valid_sequence(12, 12, z):
                        print(
                            first_five
                            + six_seven
                            + eight_nine_ten
                            + eleven
                            + twelve
                            + thirteen
                            + "?",
                            end="\r",
                        )
                        for fourteen, z in get_valid_sequence(13, 13, z):
                            print()
                            if z == 0:
                                solution = (
                                    first_five
                                    + six_seven
                                    + eight_nine_ten
                                    + eleven
                                    + twelve
                                    + thirteen
                                    + fourteen
                                )
                                print(solution)
                                print(execute_program(data, solution))
                                pass
