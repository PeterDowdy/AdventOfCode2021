data = []
with open('day10.txt') as f:
    for x in f.readlines():
        data.append(x.strip())

incompletes = []
for line in data:
    parse_stack = []
    invalid = False
    for c in line:
        if len(parse_stack) == 0:
            parse_stack.append(c)
        else:
            if ((parse_stack[-1] == '[' and c == ']')
            or (parse_stack[-1] == '<' and c == '>')
            or (parse_stack[-1] == '{' and c == '}')
            or (parse_stack[-1] == '(' and c == ')')):
                parse_stack.pop()
            elif c in ")]}>":
                invalid = True
                break
            else:
                parse_stack.append(c)
    if len(parse_stack) > 0 and not invalid:
        incompletes.append(''.join(parse_stack))


scores = []
for incomplete in incompletes:
    score = 0
    for c in incomplete[::-1]:
        score *= 5
        if c == '(':
            score += 1
        elif c == '[':
            score += 2
        elif c == '{':
            score += 3
        elif c == '<':
            score += 4
    scores.append(score)

scores = list(sorted(scores))
print(scores[len(scores)//2])