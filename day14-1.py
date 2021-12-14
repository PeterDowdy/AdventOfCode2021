from typing import Counter


data = []
with open("day14.txt") as f:
    for x in f.readlines():
        data.append(x.strip())

current = data[0]
rules = {}
for row in data[1:]:
    if " -> " not in row:
        continue
    toks = row.split(" -> ")
    rules[toks[0]] = toks[1]

for n in range(0, 10):
    next_phase = ""
    for n in range(0, len(current) - 1):
        pair = current[n] + current[n + 1]
        if pair in rules:
            next_phase += current[n] + rules[pair]
    current = next_phase + current[-1]

count = Counter(current)
counts = sorted(v for v in count.values())
print(counts[-1] - counts[0])
