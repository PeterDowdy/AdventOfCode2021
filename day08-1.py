data = []
with open('day8.txt') as f:
    for x in f.readlines():
        data.append(x.strip())

count_of_1_4_7_8 = 0
for line in data:
    tokens = line.split(' | ')
    input = tokens[0].split(' ')
    output = tokens[1].split(' ')
    for o in output:
        if len(o) in (2,3,4,7):
            count_of_1_4_7_8 += 1

print(count_of_1_4_7_8)