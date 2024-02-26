# 틱택토

import sys
answer = []

def check(game, X_cnt, O_cnt) :
    if X_cnt == O_cnt + 1 :
        win = 'X'
    else:
        win = 'O'
    
    X_win = False
    O_win = False

    for i in game:
        if i.count(i[0]) == 3 :
            if i[0] == 'O' :
                O_win = True
            elif i[0] == 'X' :
                X_win = True       
    
    if X_win and O_win :
        return "invalid"
    
    for i in range(3):
        if game[0][i] == game[1][i] == game[2][i]:
            if game[0][i] == 'O' :
                O_win = True
            elif game[0][i] == 'X':
                X_win = True
    
    if X_win and O_win :
        return "invalid"
    
    if game[0][0] == game[1][1] == game[2][2] or game[0][2] == game[1][1] == game[2][0] :
        if game[1][1] == 'O' :
            O_win = True
        elif game[1][1] == 'X':
            X_win = True

    if X_win and O_win :
        return "invalid"
    
    if (X_win and not O_win) or (not X_win and O_win) :
        if (X_win and win == 'O') or (O_win and win == 'X'):
            return "invalid"
        else: 
            return "valid"
    elif not X_win and not O_win and X_cnt == 5 and O_cnt == 4:
        return "valid"
    
    return "invalid"

while True:
    input = sys.stdin.readline().strip()
    if input == 'end':
        break

    # X, O, . 갯수 확인
    X_cnt = input.count('X')
    O_cnt = input.count('O')
    if X_cnt != O_cnt + 1 and X_cnt != O_cnt:
        answer.append("invalid")
        continue

    game = [input[i : i+3] for i in range(0, 9, 3)]
    answer.append(check(game, X_cnt, O_cnt))

print(*answer, sep="\n")