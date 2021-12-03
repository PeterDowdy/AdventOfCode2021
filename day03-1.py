data = []
with open('day3.txt') as f:
    for x in f.readlines():
        data.append(x.strip())

gamma_epsilon = {}

for binary in data:
    for x in range(0,len(binary)):
        bit = binary[x]
        if x not in gamma_epsilon:
            gamma_epsilon[x] = (0,0)
        if bit == '0':
            gamma_epsilon[x] = (gamma_epsilon[x][0],gamma_epsilon[x][1]+1)
        else:
            gamma_epsilon[x] = (gamma_epsilon[x][0]+1,gamma_epsilon[x][1])

gamma = ''
epsilon = ''

for n in range(0, len(data[0])):
    pos,neg = gamma_epsilon[n]
    if pos > neg:
        gamma += '1'
        epsilon += '0'
    else:
        gamma += '0'
        epsilon += '1'

print(int(gamma,2)*int(epsilon,2))