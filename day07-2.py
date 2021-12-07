from collections import Counter
from math import floor,ceil
data = []
with open('day7.txt') as f:
    for x in f.readlines():
        data.append(x.strip())

crabs = [int(x) for x in data[0].split(',')]

dist_lookups = {0:0, 1:1}
for n in range(2,2*max(crabs)):
    dist_lookups[n] = dist_lookups[n-1]+n
distances = []
for x in range(0,max(crabs)):
    distance = 0
    for c in crabs:        
        distance += dist_lookups[abs(c-x)]
    distances.append(distance)

print(min(distances))