# 파도반 수열

T = int(input())
inp = []
for test in range(T):
    N = int(input())
    inp.append(N)
P = [1, 1, 1] + [0] * (max(inp) - 3)
for i in range(3, max(inp)):
    P[i] = P[i-2] + P[i-3]
for i in inp:
    print(P[i-1])