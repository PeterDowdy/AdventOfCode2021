from collections import Counter
from math import floor,ceil
data = []
with open('day7.txt') as f:
    for x in f.readlines():
        data.append(x.strip())

crabs = [int(x) for x in data[0].split(',')]


distances = []
for x in range(0,max(crabs)):
    distance = 0
    for c in crabs:
        distance += abs(c-x)
    distances.append(distance)

print(min(distances))