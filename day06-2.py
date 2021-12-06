from collections import Counter

data = []
with open('day6.txt') as f:
    for x in f.readlines():
        data.append(x.strip())


fishes = {int(k):v for k,v in Counter(data[0].replace(',','')).items()}

for n in range(0,256):
    next_fishes = {}
    for k,v in fishes.items():
        if k == 0:
            if 6 not in next_fishes:
                next_fishes[6] = 0
            if 8 not in next_fishes:
                next_fishes[8] = 0
            next_fishes[8] += v
            next_fishes[6] += v
        else:
            if k-1 not in next_fishes:
                next_fishes[k-1] = 0
            next_fishes[k-1] += v
    fishes = next_fishes
        

print(sum(x for x in fishes.values()))