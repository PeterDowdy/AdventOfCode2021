data = []
with open('day8.txt') as f:
    for x in f.readlines():
        data.append(x.strip())

sums = 0
for line in data:
    tokens = line.split(' | ')
    input = tokens[0].split(' ')
    output = tokens[1].split(' ')
    possibilities = {
        k: list('abcdefg')
        for k in 'abcdefg'
        }
    for o in sorted(input,key=lambda x: len(x)):
        if len(o) == 2:
            possibilities['a'] = [x for x in possibilities['a'] if x not in o]
            possibilities['b'] = [x for x in possibilities['b'] if x not in o]
            possibilities['c'] = [x for x in possibilities['c'] if x in o]
            possibilities['d'] = [x for x in possibilities['d'] if x not in o]
            possibilities['e'] = [x for x in possibilities['e'] if x not in o]
            possibilities['f'] = [x for x in possibilities['f'] if x in o]
            possibilities['g'] = [x for x in possibilities['g'] if x not in o]
        if len(o) == 3:
            possibilities['a'] = [x for x in possibilities['a'] if x in o]
            possibilities['b'] = [x for x in possibilities['b'] if x not in o]
            possibilities['c'] = [x for x in possibilities['c'] if x in o]
            possibilities['d'] = [x for x in possibilities['d'] if x not in o]
            possibilities['e'] = [x for x in possibilities['e'] if x not in o]
            possibilities['f'] = [x for x in possibilities['f'] if x in o]
            possibilities['g'] = [x for x in possibilities['g'] if x not in o]
        if len(o) == 4:
            possibilities['a'] = [x for x in possibilities['a'] if x not in o]
            possibilities['b'] = [x for x in possibilities['b'] if x in o]
            possibilities['c'] = [x for x in possibilities['c'] if x in o]
            possibilities['d'] = [x for x in possibilities['d'] if x in o]
            possibilities['e'] = [x for x in possibilities['e'] if x not in o]
            possibilities['f'] = [x for x in possibilities['f'] if x in o]
            possibilities['g'] = [x for x in possibilities['g'] if x not in o]
        if len(o) == 5:
            if not any(o_ in possibilities['b'] for o_ in o) and not any(o_ in possibilities['f'] for o_ in o):
                #it's 2
                possibilities['a'] = [x for x in possibilities['a'] if x in o]
                possibilities['b'] = [x for x in possibilities['b'] if x not in o]
                possibilities['c'] = [x for x in possibilities['c'] if x in o]
                possibilities['d'] = [x for x in possibilities['d'] if x in o]
                possibilities['e'] = [x for x in possibilities['e'] if x in o]
                possibilities['f'] = [x for x in possibilities['f'] if x not in o]
                possibilities['g'] = [x for x in possibilities['g'] if x in o]
            if not any(o_ in possibilities['b'] for o_ in o) and not any(o_ in possibilities['e'] for o_ in o):
                #it's 3
                possibilities['a'] = [x for x in possibilities['a'] if x in o]
                possibilities['b'] = [x for x in possibilities['b'] if x not in o]
                possibilities['c'] = [x for x in possibilities['c'] if x in o]
                possibilities['d'] = [x for x in possibilities['d'] if x in o]
                possibilities['e'] = [x for x in possibilities['e'] if x not in o]
                possibilities['f'] = [x for x in possibilities['f'] if x in o]
                possibilities['g'] = [x for x in possibilities['g'] if x in o]
            if not any(o_ in possibilities['c'] for o_ in o) and not any(o_ in possibilities['e'] for o_ in o):
                #it's 5
                possibilities['a'] = [x for x in possibilities['a'] if x in o]
                possibilities['b'] = [x for x in possibilities['b'] if x in o]
                possibilities['c'] = [x for x in possibilities['c'] if x not in o]
                possibilities['d'] = [x for x in possibilities['d'] if x in o]
                possibilities['e'] = [x for x in possibilities['e'] if x not in o]
                possibilities['f'] = [x for x in possibilities['f'] if x in o]
                possibilities['g'] = [x for x in possibilities['g'] if x in o]
        if len(o) == 6:
            if not any(o_ in possibilities['d'] for o_ in o):
                #it's 0
                possibilities['a'] = [x for x in possibilities['a'] if x in o]
                possibilities['b'] = [x for x in possibilities['b'] if x in o]
                possibilities['c'] = [x for x in possibilities['c'] if x in o]
                possibilities['d'] = [x for x in possibilities['d'] if x not in o]
                possibilities['e'] = [x for x in possibilities['e'] if x in o]
                possibilities['f'] = [x for x in possibilities['f'] if x in o]
                possibilities['g'] = [x for x in possibilities['g'] if x in o]
            if not any(o_ in possibilities['c'] for o_ in o):
                #it's 6
                possibilities['a'] = [x for x in possibilities['a'] if x in o]
                possibilities['b'] = [x for x in possibilities['b'] if x in o]
                possibilities['c'] = [x for x in possibilities['c'] if x not in o]
                possibilities['d'] = [x for x in possibilities['d'] if x in o]
                possibilities['e'] = [x for x in possibilities['e'] if x in o]
                possibilities['f'] = [x for x in possibilities['f'] if x in o]
                possibilities['g'] = [x for x in possibilities['g'] if x in o]
            if not any(o_ in possibilities['e'] for o_ in o):
                #it's 9
                possibilities['a'] = [x for x in possibilities['a'] if x in o]
                possibilities['b'] = [x for x in possibilities['b'] if x in o]
                possibilities['c'] = [x for x in possibilities['c'] if x in o]
                possibilities['d'] = [x for x in possibilities['d'] if x in o]
                possibilities['e'] = [x for x in possibilities['e'] if x not in o]
                possibilities['f'] = [x for x in possibilities['f'] if x in o]
                possibilities['g'] = [x for x in possibilities['g'] if x in o]
    
    #map to abcdef
    deductions = [[x] for x in possibilities['a']]
    for cur in 'bcdefg':
        next_deductions = []
        for n in possibilities[cur]:
            for d in deductions:
                next_deductions += [d + [n]]
        deductions = [x for x in next_deductions if len(list(set(x))) == len(x)]

    for deduction in deductions:
        conclusions = [
            deduction[0]+deduction[1]+deduction[2]+deduction[4]+deduction[5]+deduction[6],
            deduction[2]+deduction[5],
            deduction[0]+deduction[2]+deduction[3]+deduction[4]+deduction[6],
            deduction[0]+deduction[2]+deduction[3]+deduction[5]+deduction[6],
            deduction[1]+deduction[2]+deduction[3]+deduction[5],
            deduction[0]+deduction[1]+deduction[3]+deduction[5]+deduction[6],
            deduction[0]+deduction[1]+deduction[3]+deduction[4]+deduction[5]+deduction[6],
            deduction[0]+deduction[2]+deduction[5],
            deduction[0]+deduction[1]+deduction[2]+deduction[3]+deduction[4]+deduction[5]+deduction[6],
            deduction[0]+deduction[1]+deduction[2]+deduction[3]+deduction[5]+deduction[6],
        ]
        valid = True
        for c in conclusions:
            if ''.join(sorted(c)) not in [''.join(sorted(i)) for i in input]:
                valid = False
                break
            # if ''.join(sorted(c)) not in [''.join(sorted(o)) for o in input]:
            #     valid = False
            #     break

        if valid:
            break
    decoded = {''.join(sorted(c)):str(ix) for ix,c in enumerate(conclusions)}
    number = ''
    for o in output:
        number += decoded[''.join(sorted(o))]
    print(number)
    sums += int(number)
print(sums)