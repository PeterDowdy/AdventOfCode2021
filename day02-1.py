data = []
with open('day2.txt') as f:
    data = [x.strip() for x in f.readlines()]

horiz = 0
depth = 0

for instr in data:
    if 'up' in instr:
        depth -= int(instr.split(' ')[1])
        if depth < 0:
            depth = 0
    if 'down' in instr:
        depth += int(instr.split(' ')[1])
    if 'forward' in instr:
        horiz += int(instr.split(' ')[1])

print(horiz*depth)