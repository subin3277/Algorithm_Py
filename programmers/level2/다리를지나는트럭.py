# 다리를 지나는 트럭

from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = deque([0]*bridge_length)
    truck = deque(truck_weights)
    weight_sum = 0
    
    while truck:
        move = bridge.popleft()
        weight_sum -= move
        if truck[0] + weight_sum <= weight :
            t = truck.popleft()
            bridge.append(t)
            weight_sum += t
        else:
            bridge.append(0)
        answer += 1
        
    while bridge and weight_sum!= 0:
        t = bridge.popleft()
        weight_sum -= t
        answer += 1
    
    return answer