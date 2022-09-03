# 나이순 정렬
import sys
sys.stdin = open("input.txt", "r")

N = int(input())
age_list = []
name_list = []
for i in range(N):
    A, B = map(str, input().split())
    age_list.append(A)
    name_list.append(B)
sol = []
# 정렬하기
for i in range(N):
    minidx = age_list.index(min(age_list))
    sol.append((age_list.pop(minidx), name_list.pop(minidx)))

for i in range(N):
    print(*sol[i])