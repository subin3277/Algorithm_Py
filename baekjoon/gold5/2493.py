import sys
sys.stdin = open("input.txt", "r")

N = int(input())
from collections import deque
lst = list(map(int, input().split()))
ans = deque([0])
hs = deque([(lst[0],1)])
for i in range(1, N):
    if lst[i]<=lst[i-1]: # 앞 건물보다 같거나 작을 경우
        ans.append(i) # 답 갱신
        hs.append((lst[i], i+1)) # h 리스트에 (높이, 인덱스 +1) 추가
    else:
        while hs and hs[-1][0] < lst[i] : # 해당 건물보다 작은 건물은 가려짐. h 리스트에서 제외.
            hs.pop()
        if hs:
            ans.append(hs[-1][1]) # 자기보다 높은 건물이 있을 경우 답 갱신
        else:
            ans.append(0) # 자기보다 높은 건물이 없을 경우 0 추가
        hs.append((lst[i], i+1)) # h 리스트에 (높이, 인덱스 +1) 추가
print(*ans)