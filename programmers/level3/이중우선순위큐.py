import heapq

def solution(operations):
    answer = [0, 0]
    heap_max = []
    heap_min = []
    for i in operations :
        num = int(i.split(' ')[1])
        if (i[0] == 'I'):
            # 숫자 삽입
            heapq.heappush(heap_min, num)
            heapq.heappush(heap_max, (-num, num))
        else :
            if heap_max and heap_min and num == -1:
                # 최솟값 삭제
                t = heapq.heappop(heap_min)
                heap_max.remove((-t, t))
            elif heap_max and heap_min and num == 1 :
                # 최댓값 삭제
                t = heapq.heappop(heap_max)[1]
                heap_min.remove(t)
    if heap_min :
        answer = [heapq.heappop(heap_max)[1], heapq.heappop(heap_min)]
    return answer

oper = ["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]
print(solution(oper))