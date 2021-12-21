from itertools import *
import heapq
from collections import *
import ast
from typing import Any
import numpy as np

player_1 = 4
player_2 = 1

roll_count = 0
die = 1

player_1_score = 0
player_2_score = 0

whose_turn = 1
while True:
    roll_count += 3
    move = die + die + die + 1 + 2
    die += 3
    if whose_turn == 1:
        player_1 += move
        while player_1 > 10:
            player_1 = player_1 - 10
        player_1_score += player_1
        whose_turn = 2
    elif whose_turn == 2:
        player_2 += move
        while player_2 > 10:
            player_2 = player_2 - 10
        player_2_score += player_2
        whose_turn = 1
    if player_1_score >= 1000 or player_2_score >= 1000:
        break

print(min([player_1_score, player_2_score]) * roll_count)
