# 최소 신장 트리
import sys
sys.stdin = open("input.txt", "r")

def prim1(r, V):
    MST = [0]*(V+1)     # MST 포함여부
    key = [10000]*(V+1) # 가중치의 최대값 이상으로 초기화. key[v]는 v가 MST에 속한 정점과 연결될 때의 가중치
    key[r] = 0          # 시작정점의 key
    for _ in range(V):  # V+1개의 정점 중 V개를 선택
        # MST에 포함되지 않은 정점 중(MST[u]==0), key가 최소인 u 찾기
        u = 0
        minV = 10000
        for i in range(V+1):
            if MST[i]==0 and key[i]< minV:
                u = i
                minV = key[i]
        MST[u] = 1                  # 정점 u를 MST에 추가
        # u에 인접인 v에 대해, MST에 포함되지 않은 정점이면
        for v in range(V+1):
            if MST[v]==0 and adjM[u][v]>0:
                key[v] = min(key[v], adjM[u][v])     # u를 통해 MST에 포함되는 비용과 기존 비용을 비교, 갱신
    return sum(key)         # MST 가중치의 합

T = int(input())
for test in range(1, T + 1):
    V, E = map(int, input().split())
    adjM = [[0] * (V+1) for _ in range(V+1)]
    adjL = [[] for _ in range(V+1)]
    for _ in range(E):
        n1, n2, w = map(int, input().split())
        adjM[n1][n2] = w
        adjM[n2][n1] = w
        adjL[n1].append((n2, w))
        adjL[n2].append((n1, w))
    print(f'#{test}', prim1(0, V))
