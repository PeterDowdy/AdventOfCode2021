data = []
with open('day10.txt') as f:
    for x in f.readlines():
        data.append(x.strip())

score = 0
for line in data:
    parse_stack = []
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
                if c == ')':
                    score += 3
                if c == ']':
                    score += 57
                if c == '}':
                    score += 1197
                if c == '>':
                    score += 25137
                break
            else:
                parse_stack.append(c)

print(score)

