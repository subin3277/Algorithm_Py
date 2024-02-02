# 우리집엔 도서관이 있어
N = int(input())
book = [int(input()) for _ in range(N)]

bottom = book.index(N)
maxbook = N
answer = N - bottom - 1
for i in range(bottom - 1, -1, -1) :
    if book[i] != maxbook -1 :
        answer += 1
    else :
        maxbook = book[i]

print(answer)