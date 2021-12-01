data = []
with open('day1.txt') as f:
    data = [x.strip() for x in f.readlines()]

increases = 0

for x in range(0,len(data)-1):
    if int(data[x])<int(data[x+1]):
        increases += 1

print(increases)