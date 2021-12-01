data = []
with open('day1.txt') as f:
    data = [x.strip() for x in f.readlines()]

increases = 0

for x in range(0,len(data)-3):
    window_one = int(data[x])+int(data[x+1])+int(data[x+2])
    window_two = int(data[x+1])+int(data[x+2])+int(data[x+3])
    if window_two > window_one:
        increases += 1

print(increases)