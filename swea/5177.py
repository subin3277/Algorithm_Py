# 이진 힙
import sys
sys.stdin = open("input.txt", "r")

def enq(n): # 힙에 삽입
    global last
    last += 1
    heap[last] = n
    c = last
    p = c//2
    while p and heap[p] > heap[c]:
        heap[p], heap[c] = heap[c], heap[p]
        c = p
        p = c//2

T = int(input())
for test in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))
    heap = [0] * (N+1)
    last = 0
    for i in lst: # 순서대로 삽입
        enq(i)
    ans = 0
    p = N // 2
    while p: # 조상 노드들 합
        ans += heap[p]
        p = p//2
    print(f'#{test} {ans}')