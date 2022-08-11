# 특별한 정렬
import sys
sys.stdin = open("input.txt", "r")

def bubblesort(N): # 버블정렬 이용하여 정렬
    for i in range(len(N)-1,-1,-1):
        for j in range(i):
            if N[j] > N[j+1]:
                N[j], N[j+1] = N[j+1], N[j]
    return N

T = int(input())
for test in range(1, T+1):
    N = int(input())
    num_list = list(map(int, input().split()))
    num_list = bubblesort(num_list) # 오름차순 정렬

    res_list = [0]*N
    for i in range(0,N,2):
        res_list[i] = num_list[N-1-(i//2)] # 짝수 index 값 넣기
        res_list[i+1] = num_list[i//2] # 홀수 index 값 넣기
    res_list = res_list[:10] # 10번째 까지만 자르기
    print(f'#{test}', *res_list)