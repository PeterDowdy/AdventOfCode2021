data = []
with open('day9.txt') as f:
    for x in f.readlines():
        data.append([int(y) for y in x.strip()])

coords = {}

for y in range(0,len(data)):
    for x in range(0,len(data[0])):
        coords[(x,y)] = data[y][x]

lowests = []

for k in coords.keys():
    neighbours = [(k[0]+1,k[1]),(k[0]-1,k[1]),(k[0],k[1]+1),(k[0],k[1]-1)]
    neighbour_lower = False
    for n in neighbours:
        if n not in coords:
            pass
        elif coords[n] <= coords[k]:
            neighbour_lower = True
    if not neighbour_lower:
        lowests.append(coords[k])

print(sum([x+1 for x in lowests]))
