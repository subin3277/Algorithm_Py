# 비밀번호 찾기
import sys
input = sys.stdin.readline
N, M = map(int, input().split())

dict = {}
for _ in range(N):
    web, password = map(str, input().split())
    dict[web] = password
    dict[password] = web
for _ in range(M):
    question = input().rstrip()
    print(dict[question])