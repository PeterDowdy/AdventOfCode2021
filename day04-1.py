data = []
with open('day4.txt') as f:
    for x in f.readlines():
        data.append(x.strip())

drawings = data[0].split(',')
boards = []
current_board = []
for n in range(1,len(data)):
    if data[n] == '':
        continue
    else:
        current_board += [(x,False) for x in data[n].split(' ') if x != '']
        if len(current_board) == 25:
            boards.append(current_board)
            current_board = []

for drawing in drawings:
    for board in boards:
        for n in range(0,len(board)):
            pos = board[n]
            if pos[0] == drawing:
                board[n] = (pos[0], True)
        blah = board[0:5]
        if (all(x[1] for x in board[0:5])
        or all(x[1] for x in board[5:10])
        or all(x[1] for x in board[10:15])
        or all(x[1] for x in board[15:20])
        or all(x[1] for x in board[20:25])
        or all(x[1] for x in [board[y*5] for y in range(0,5)])
        or all(x[1] for x in [board[1+y*5] for y in range(0,5)])
        or all(x[1] for x in [board[2+y*5] for y in range(0,5)])
        or all(x[1] for x in [board[3+y*5] for y in range(0,5)])
        or all(x[1] for x in [board[4+y*5] for y in range(0,5)])
        or all(x[1] for x in [board[6*y] for y in range(0,5)])
        or all(x[1] for x in [board[4],board[8],board[12],board[16],board[20]])):
            print('win!')
            buf = ''
            for x in range(0,5):
                for y in range(0,5):
                    buf += (' ')
                    if board[x*5+y][1]:
                        buf += ('*')
                    else:
                        buf += ('-')
                    buf += (board[x*5+y][0])
                buf += ('\n')
            
            print(buf)
            print(sum([int(x[0]) for x in board if not x[1]])*int(drawing))