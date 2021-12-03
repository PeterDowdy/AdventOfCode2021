data = []
with open('day3.txt') as f:
    for x in f.readlines():
        data.append(x.strip())

oxygens = [x for x in data]

oxygen_canonical = ''
while len(oxygens) > 1:
    pos = 0
    neg = 0
    for binary in oxygens:
        if binary[len(oxygen_canonical)] == '1':
            pos += 1
        else:
            neg += 1
    if pos >= neg:
        oxygen_canonical += '1'
    else:
        oxygen_canonical += '0'
    oxygens = [x for x in oxygens if x.startswith(oxygen_canonical)]

print(int(oxygens[0],2))


carbons = [x for x in data]

carbon_canonical = ''
while len(carbons) > 1:
    pos = 0
    neg = 0
    for binary in carbons:
        if binary[len(carbon_canonical)] == '1':
            pos += 1
        else:
            neg += 1
    if neg <= pos:
        carbon_canonical += '0'
    else:
        carbon_canonical += '1'
    carbons = [x for x in carbons if x.startswith(carbon_canonical)]

print(int(carbons[0],2))

print(int(oxygens[0],2)*int(carbons[0],2))