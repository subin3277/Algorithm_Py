# K번째 수

import heapq

def solution(array, commands):
    answer = []
    for i, j, k in commands:
        heap = []
        for ii in range(i-1, j):
            heapq.heappush(heap, array[ii])
        for _ in range(k):
            t = heapq.heappop(heap)
        answer.append(t)
    return answer