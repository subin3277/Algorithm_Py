# 프렌즈 4블록

def solution(m, n, board):
    answer = 0
    new_board = []
    for i in board:
        new_board.append(list(i))
    print(new_board)
    return answer

m = 6
n = 6
board = ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]
print(solution(m, n, board)) #14