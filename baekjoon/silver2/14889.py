# 스타트와 링크
from itertools import combinations

N = int(input())
num = []
for _ in range(N):
    num.append(list(map(int, input().split())))
people = [] # 사람 번호 저장할 리스트
for i in range(1, N+1):
    people.append(i)

res = [] # 능력치 차이 저장할 리스트
for c in combinations(people, N//2): # N//2개로 이루어져있는 모든 조합
    start = list(c)
    link = []
    for i in people: # 스타트에 없는 사람은 링크에 저장
        if not i in start:
            link.append(i)

    startres = linkres = 0 # 각각의 능력치합 저장할 변수
    for i in range(N//2 - 1):
        for j in range(i+1, N//2): # 능력치 합 구하기
            startres += num[start[i]-1][start[j]-1] + num[start[j]-1][start[i]-1]
            linkres += num[link[i]-1][link[j]-1] + num[link[j]-1][link[i]-1]
    res.append(abs(startres - linkres)) # 두 능력치의 차이 저장

print(min(res)) # 최소 차이 출력
