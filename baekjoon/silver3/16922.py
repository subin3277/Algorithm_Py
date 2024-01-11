# 로마 숫자 만들기
N = int(input())
num = [1, 5, 10, 50]
answer = set()

def BT(index, res):
    global answer
    if len(res) == N:
        answer.add(sum(res))
        return
    for i in range(index, 4):
        BT(i, [*res, num[i]])

BT(0, [])
print(len(answer))