# 병합 정렬
import sys
sys.stdin = open("input.txt", "r")

def merge_sort(arr):
    global ans
    if len(arr) < 2:
        return arr

    mid = len(arr) // 2 # 두개로 나누기
    left_arr = merge_sort(arr[:mid])
    right_arr = merge_sort(arr[mid:])

    merged_arr = []
    l = h = 0
    while l < len(left_arr) and h < len(right_arr): # 다시 합치기
        if left_arr[l] < right_arr[h]:
            merged_arr.append(left_arr[l])
            l += 1
        else:
            merged_arr.append(right_arr[h])
            h += 1
    if left_arr[-1] > right_arr[-1]:
        ans += 1
    merged_arr += left_arr[l:]
    merged_arr += right_arr[h:]
    return merged_arr

T = int(input())
for test in range(1, T + 1):
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    A = merge_sort(A)
    print(f'#{test}', A[N//2], ans)