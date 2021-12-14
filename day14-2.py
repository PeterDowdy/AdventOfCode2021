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

current_count = Counter()
for n in range(0, len(current) - 1):
    pair = current[n] + current[n + 1]
    current_count[pair] += 1

for n in range(0, 40):
    print(f"phase {n}")
    next_count = Counter()
    for pair, count in current_count.items():
        next_count[pair[0] + rules[pair]] += count
        next_count[rules[pair] + pair[1]] += count

    current_count = next_count

final_count = Counter()
for k, v in current_count.items():
    final_count[k[0]] += v
final_count[current[-1]] += 1
counts = sorted(v for v in final_count.values())
print(counts[-1] - counts[0])
