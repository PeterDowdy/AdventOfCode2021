data = []
with open("day13.txt") as f:
    for x in f.readlines():
        data.append(x.strip())

points = []
folds = []
for c in data:
    if "fold" not in c and len(c) > 0:
        toks = c.split(",")
        points.append((int(toks[0]), int(toks[1])))
    elif "fold" in c:
        toks = c.split(" ")[-1]
        toks = toks.split("=")
        folds.append((toks[0], int(toks[1])))

points = set(points)
f = folds[0]
next_points = []
if f[0] == "x":
    for k in points:
        if k[0] > f[1]:
            next_points.append((f[1] + (f[1] - k[0]), k[1]))
        else:
            next_points.append(k)
elif f[0] == "y":
    for k in points:
        if k[1] > f[1]:
            next_points.append((k[0], f[1] + (f[1] - k[1])))
        else:
            next_points.append(k)
    pass
points = set(next_points)
print(len(points))
