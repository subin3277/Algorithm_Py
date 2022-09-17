#듣보잡
N, M = map(int, input().split())
name1 = set()
name2 = set()
for _ in range(N):
    name1.add(input())
for _ in range(M):
    name2.add(input())
res = sorted(list(name1&name2))
print(len(res))
for i in res:
    print(i)