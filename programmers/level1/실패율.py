# 실패율

def solution(N, stages):
    answer = []
    chal = [0] * (N+1)
    suc = [0] * (N+1)
    for i in range(1, N+1):
        tmp = stages.count(i)
        chal[i] = tmp
        suc[i] = tmp
    chal[N] += stages.count(N+1)

    print(chal)
    print(suc)

    for i in range(1, N+1):
        tmp = sum(chal[i::])
        if tmp == 0:
            suc[i] = 0
        else:
            suc[i] = suc[i] / tmp

    suc = suc[1::]
    for i in range(N):
        answer.append(suc.index(max(suc)) + 1)
        suc[suc.index(max(suc))] = -1
    return answer

N = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]
print(solution(N, stages))