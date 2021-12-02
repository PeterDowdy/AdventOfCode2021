data = []
with open('day2.txt') as f:
    data = [x.strip() for x in f.readlines()]

horiz = 0
depth = 0
aim = 0

for instr in data:
    if 'up' in instr:
        aim -= int(instr.split(' ')[1])
    if 'down' in instr:
        aim += int(instr.split(' ')[1])
    if 'forward' in instr:
        horiz += int(instr.split(' ')[1])
        depth += int(instr.split(' ')[1])*aim

print(horiz*depth)