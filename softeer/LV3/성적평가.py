# 성적 평가
def getscore(N, score):
    tmp = [N] * N
    for i in range(len(score)-1):
        for j in range(i+1, len(score)):
            if score[i] > score[j]:
                tmp[i] -= 1
            elif score[i] == score[j]:
                tmp[i] -= 1
                tmp[j] -= 1
            else:
                tmp[j] -= 1
    return tmp

N = int(input())
score = [list(map(int, input().split())) for _ in range(N)]

sumscore = [0] * N

for i in score:
    print(*getscore(N, i))
    for j in range(len(score)):
        sumscore[j] += i[j]
print(*getscore(N, sumscore))

