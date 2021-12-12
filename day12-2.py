import heapq

data = []
with open('day12.txt') as f:
    for x in f.readlines():
        data.append(x.strip())

links = {}
for path in data:
    toks = path.split('-')
    if toks[0] not in links:
        links[toks[0]] = []
    links[toks[0]].append(toks[1])
    if toks[1] not in links:
        links[toks[1]] = []
    links[toks[1]].append(toks[0])

links = {k:list(set(v)) for k,v in links.items()}

candidates = [['start']]

finished_paths = []
while len(candidates) > 0:
    next_paths = []
    for c in candidates:
        currently = c[-1]
        if currently == 'end':
            finished_paths.append(c)
        else:
            next_candidates = links[currently]
            for next_c in next_candidates:
                if next_c == 'start':
                    pass
                elif all(letter in 'abcdefghijklmnopqrstuvwxyz' for letter in next_c) and next_c in c and 'revisited' in c:
                    pass
                else:
                    if all(letter in 'abcdefghijklmnopqrstuvwxyz' for letter in next_c) and next_c in c:
                        next_paths.append(['revisited'] + c + [next_c])
                    else:
                        next_paths.append(c + [next_c])
    candidates = next_paths

print(len(finished_paths))