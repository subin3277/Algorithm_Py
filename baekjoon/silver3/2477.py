# 참외밭
import sys
sys.stdin = open("input.txt", "r")

K = int(input())
# 동쪽은 1, 서쪽은 2, 남쪽은 3, 북쪽은 4
len_list = [0]*4 # 네변의 길이 저장할 리스트
small_len = [0]*4 # 작은 직사각형 길이 저장할 리스트
for _ in range(6):
    A, B = map(int, input().split())
    if len_list[A-1] != 0: # 이미 값이 있다면
        small_len[A//3] = len_list[A-1]
        small_len[A//3+1] = B
    len_list[A-1] += B
res = (len_list[1]*len_list[3]) - (small_len[1]*small_len[2]) # 큰 직사각형에서 작은 직사각형 빼주기
print(res*K) # 한칸에 자라는 참외 개수 곱해주기
# 해결못함~~~~~~~~~~~~~~~~~~~~~~~~~