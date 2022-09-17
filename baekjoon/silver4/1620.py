# 나는야 포켓몬 마스터 이다솜
import sys

input1 = sys.stdin.readline
N, M = map(int, input().split())

pocket = {}
for i in range(1, N+1):
    tmp = input().rstrip()
    pocket[str(i)] = tmp
    pocket[tmp] = str(i)
for _ in range(M):
    question = input().rstrip()
    print(pocket[question])