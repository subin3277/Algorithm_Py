# 부분수열의 합
N, S = map(int, input().split())
num = list(map(int, input().split()))
num.sort()
answer = 0
answer_lst = [0] * N
def BT(index, sum) :
    global answer
    if index >= N :
        return
    sum += num[index]
    if sum == S:
        answer += 1
    BT(index+1, sum-num[index])
    BT(index+1, sum)

BT(0, 0)
print(answer)