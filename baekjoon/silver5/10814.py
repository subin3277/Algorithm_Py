# 나이순 정렬
import sys
sys.stdin = open("input.txt", "r")

N = int(input())
input_list = []
for i in range(N):
    A, B = map(str, input().split())
    input_list.append([int(A), B])

input_list.sort(key = lambda x:x[0])

for i in input_list:
    print(i[0], i[1])