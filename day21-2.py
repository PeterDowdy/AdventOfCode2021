from itertools import *
import heapq
from collections import *
import ast
from typing import Any
import numpy as np
from functools import lru_cache

winners = {1: 0, 2: 0}

seen_games = {}


def take_turn(player_1, player_2, player_1_score, player_2_score, whose_turn):
    continued_games = {}
    player_1_gains = 0
    player_2_gains = 0
    for move, freq in [(6, 7), (5, 6), (7, 6), (4, 3), (8, 3), (3, 1), (9, 1)]:
        _move = move
        _whose_turn = whose_turn
        _player_1 = player_1
        _player_1_score = player_1_score
        _player_2 = player_2
        _player_2_score = player_2_score
        if whose_turn == 1:
            _player_1 += _move
            while _player_1 > 10:
                _player_1 = _player_1 - 10
            _player_1_score += _player_1
            _whose_turn = 2
        elif _whose_turn == 2:
            _player_2 += _move
            while _player_2 > 10:
                _player_2 = _player_2 - 10
            _player_2_score += _player_2
            _whose_turn = 1
        if _player_1_score >= 21:
            player_1_gains += freq
        elif _player_2_score >= 21:
            player_2_gains += freq
        else:
            continued_games[
                (
                    _player_1,
                    _player_2,
                    _player_1_score,
                    _player_2_score,
                    _whose_turn,
                )
            ] = freq
    return (player_1_gains, player_2_gains, continued_games)


games = Counter([(4, 1, 0, 0, 1)])

while len(games) > 0:
    next_games = Counter()
    for game, ct in games.items():
        if game not in seen_games:
            seen_games[game[0], game[1], game[2], game[3], game[4]] = take_turn(
                game[0], game[1], game[2], game[3], game[4]
            )
        player_1_gains, player_2_gains, continued_games = seen_games[game]
        for k, v in continued_games.items():
            next_games[k] += ct * v
        winners[1] += ct * player_1_gains
        winners[2] += ct * player_2_gains
    print(winners, end="\r")
    games = next_games
    for k, v in seen_games.items():
        player_1_score, player_2_score, next_games = v
        v_next = Counter()
        for next_game, freq in next_games.items():
            if next_game in seen_games:
                seen_1_score, seen_2_score, seen_next = seen_games[next_game]
                player_1_score += seen_1_score * freq
                player_2_score += seen_2_score * freq
                for k, v in seen_next.items():
                    v_next[k] += v * freq
            else:
                next_games[next_game] = freq

print(winners)
print(winners[1] > winners[2])
print(winners[2] > winners[1])
