data = []
with open('day6.txt') as f:
    for x in f.readlines():
        data.append(x.strip())

translation_dict = str.maketrans({"0": "68", "1": "0", "2": "1", "3": "2", "4": "3", "5": "4", "6": "5", "7": "6", "8": "7"})
fishes = data[0].replace(',','')

for n in range(0,80):
    fishes = fishes.translate(translation_dict)

print(len(fishes))