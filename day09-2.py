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
        lowests.append(k)

basins = []
for k in lowests:
    basin = set([k])
    search_space = [(k[0]+1,k[1]),(k[0]-1,k[1]),(k[0],k[1]+1),(k[0],k[1]-1)]
    while len(search_space) != 0:
        next_search_space = []
        for s in search_space:
            if s not in coords:
                pass
            elif coords[s] != 9:
                basin.add(s)
                next_search_space += [(s[0]+1,s[1]),(s[0]-1,s[1]),(s[0],s[1]+1),(s[0],s[1]-1)]

        search_space = [x for x in next_search_space if x not in basin]
    basins.append(basin)

basin_size = 1
for n in range(0,3):
    basin_size *= list(sorted([-1*len(x) for x in basins]))[n]
print(abs(basin_size))
            