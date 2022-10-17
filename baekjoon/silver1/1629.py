# 곱셈

def sol(A, B, C):
    if B == 1:
        return A % C
    if B % 2 == 0:
        return (sol(A, B//2, C) ** 2)% C
    else:
        return ((sol(A, B//2, C) ** 2) * A) % C

A, B, C = map(int, input().split())
print(sol(A, B, C))