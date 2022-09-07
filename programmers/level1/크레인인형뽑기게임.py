# 크레인 인형 뽑기게임

def solution(board, moves):
    answer = 0
    doll = []
    for i in moves:
        for j in range(len(board)):
            if board[j][i-1] != 0:
                tmp = board[j][i-1]
                board[j][i-1] = 0
                if doll and doll[-1] == tmp:
                    doll.pop()
                    answer += 2
                else:
                    doll.append(tmp)
                break
    return answer

board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]
print(solution(board, moves))