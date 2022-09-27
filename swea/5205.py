# 퀵 정렬
import sys
sys.stdin = open("input.txt", "r")

def quick_sort(array, start, end):
    if start >= end:
        return
    pivot = start
    left = start + 1
    right = end
    while(left <= right):
        while left <= end and array[left] <= array[pivot]:
            left += 1
        while right > start and array[right] >= array[pivot]:
            right -= 1
        if left > right:
            array[right], array[pivot] = array[pivot], array[right]
        else:
            array[left], array[right] = array[right], array[left]

    quick_sort(array, start, right - 1)
    quick_sort(array, right + 1, end)

T = int(input())
for test in range(1, T + 1):
    N = int(input())
    array = list(map(int, input().split()))
    quick_sort(array, 0, N - 1)
    print(f'#{test} {array[N//2]}')
