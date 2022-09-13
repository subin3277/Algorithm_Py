# 트리 순회

def preorder(n):
    if n:
        print(node[n], end="")
        preorder(ch1[n])
        preorder(ch2[n])
def inorder(n):
    if n:
        inorder(ch1[n])
        print(node[n], end="")
        inorder(ch2[n])
def postorder(n):
    if n:
        postorder(ch1[n])
        postorder(ch2[n])
        print(node[n], end="")

N = int(input())
par = [0] * (N+1)
ch1 = [0] * (N+1)
ch2 = [0] * (N+1)
node = [0]
for i in range(N):
    node.append(chr(i+65))
for i in range(N):
    P, C1, C2 = map(str, input().split())
    if C1 != ".":
        par[ord(C1)-64] = ord(P) - 64
        ch1[ord(P) - 64] = ord(C1) - 64
    if C2 != ".":
        par[ord(C2)-64] = ord(P) - 64
        ch2[ord(P) - 64] = ord(C2) - 64
preorder(1)
print()
inorder(1)
print()
postorder(1)
