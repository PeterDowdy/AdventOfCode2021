data = []
with open('day5.txt') as f:
    for x in f.readlines():
        data.append(x.strip())

overlaps = {}

for line in data:
    start,end = line.split(' -> ')
    startx,starty = start.split(',')
    endx,endy = end.split(',')
    if startx != endx and starty != endy:
        x_mod = 1
        y_mod = 1
        if int(startx) > int(endx):
            x_mod = -1
        if int(starty) > int(endy):
            y_mod = -1
        cur = (int(startx),int(starty))
        end = (int(endx),int(endy))
        while cur != end:
            if cur not in overlaps:
                overlaps[cur] = 0
            overlaps[cur] = overlaps[cur]+ 1
            cur = (cur[0]+x_mod,cur[1]+y_mod)
        if cur not in overlaps:
            overlaps[cur] = 0
        overlaps[cur] = overlaps[cur]+ 1
    elif startx != endx:
        if int(startx) > int(endx):
            swap = endx
            endx = startx
            startx = swap
        for n in range(int(startx),int(endx)+1):
            key = (n,int(starty))
            if key not in overlaps:
                overlaps[key] = 0
            overlaps[key] = overlaps[key]+ 1
    else:
        if int(starty) > int(endy):
            swap = endy
            endy = starty
            starty = swap
        for n in range(int(starty),int(endy)+1):
            key = (int(startx),n)
            if key not in overlaps:
                overlaps[key] = 0
            overlaps[key] = overlaps[key]+ 1

dangerous = 0
for v in overlaps.values():
    if v > 1:
        dangerous += 1

buf = ''
for y in range(0,10):
    for x in range(0,10):
        if (x,y) in overlaps:
            buf += str(overlaps[(x,y)])
        else:
            buf += '.'
    buf += '\n'

print(buf)

print(dangerous)