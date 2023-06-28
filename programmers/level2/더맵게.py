# 더 맵게

import heapq

def solution(scoville, K):
    answer = 0
    heap = []
    for i in scoville:
        heapq.heappush(heap, i)
    num = heap[0]
    while len(heap)>1 and num < K:
        t1 = heapq.heappop(heap)
        t2 = heapq.heappop(heap)
        heapq.heappush(heap, t1+(t2*2))
        num = heap[0]
        answer += 1
    
    if heap[0] < K:
        answer = -1
        
    return answer