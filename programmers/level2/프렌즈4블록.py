# 프렌즈 4블록

def solution(m, n, board):
    answer = 0
    new_board = []
    for i in board:
        new_board.append(list(i))

    while True:
        erase = []
        tmp = 0
        for i in range(m-1):
            for j in range(n-1):
                if new_board[i][j] != "@" and new_board[i][j] == new_board[i][j+1] == new_board[i+1][j] == new_board[i+1][j+1]:
                    erase.append((i, j))
                    tmp += 4
        if tmp == 0:
            break

        for i,j in erase:
            new_board[i][j] = new_board[i+1][j] = new_board[i][j+1] = new_board[i+1][j+1] = '@'

        for i in range(n):
            for j in range(m-1, -1, -1):
                for k in range(j):
                    if new_board[k+1][i] == "@":
                        new_board[k][i] , new_board[k+1][i] = new_board[k+1][i], new_board[k][i]
    print(new_board)
    for i in range(m):
        answer += new_board[i].count("@")
    return answer

m = 8
n = 5
board = ["HGNHU", "CRSHV", "UKHVL", "MJHQB", "GSHOT", "MQMJJ", "AGJKK", "QULKK"]
print(solution(m, n, board)) #14