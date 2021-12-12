data = []
with open('day11.txt') as f:
    for x in f.readlines():
        data.append(x.strip())

octopuses = {}
for y in range(0,10):
    for x in range(0,10):
        octopuses[(x,y)] = int(data[y][x])

flashes = 0
for n in range(0, 100):
    nextopuses = {k:v+1 for k,v in octopuses.items()}
    while any(v > 9 for v in nextopuses.values()):
        for k,v in nextopuses.items():
            if v > 9:
                flashes += 1
                for neighbour in [
                    (k[0]+1,k[1]),
                    (k[0]+1,k[1]+1),
                    (k[0],k[1]+1),
                    (k[0]-1,k[1]+1),
                    (k[0]-1,k[1]),
                    (k[0]-1,k[1]-1),
                    (k[0],k[1]-1),
                    (k[0]+1,k[1]-1)
                    ]:
                    if neighbour in nextopuses and nextopuses[neighbour] != 0:
                        nextopuses[neighbour] = nextopuses[neighbour]+1
                nextopuses[k] = 0
    octopuses = nextopuses
    buf = ''
    
    for y in range(0,10):
        for x in range(0,10):
            buf += str(octopuses[(x,y)])
        buf += '\n'
    
    print(buf)

print(flashes)