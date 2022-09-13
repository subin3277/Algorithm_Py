# 트리 순회

def preorder(n):
    if n:
        print(node[n-1])
        preorder(ch1[n-1])
        preorder(ch2[n-1])
N = int(input())
par = [0] * N
ch1 = [0] * N
ch2 = [0] * N
node = []
for i in range(N):
    P, C1, C2 = map(str, input().split())
    node.append(P)
    if C1 != ".":
        par[ord(C1)-65] = P
        ch1[ord(P) - 65] = C1
    if C2 != ".":
        par[ord(C2)-65] = P
        ch2[ord(P) - 65] = C2
preorder(1)
