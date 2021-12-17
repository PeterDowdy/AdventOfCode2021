from itertools import *
import heapq
from collections import *


# target_area = ((287, -76), (309, -48))
min_x = 287
max_x = 309
min_y = -76
max_y = -48

# min_x = 20
# max_x = 30
# min_y = -5
# max_y = 10

positions = {}

tests = []
for x in range(1, 100):
    for y in range(min_y, 100):
        tests.append((x, y))

for test in tests:
    current_pos = (0, 0)
    current_vec = test
    y_max = 0
    while True:
        current_pos = (current_pos[0] + current_vec[0], current_pos[1] + current_vec[1])
        y_max = max(y_max, current_pos[1])
        current_vec = (max(current_vec[0] - 1, 0), current_vec[1] - 1)
        if current_pos[0] > max_x or current_pos[1] < min_y:
            print("miss")
            break
        elif (
            current_pos[0] >= min_x
            and current_pos[0] <= max_x
            and current_pos[1] >= min_y
            and current_pos[1] <= max_y
        ):
            positions[test] = y_max
            print("hit")
            break

print(positions)
print(max(v for v in positions.values()))
