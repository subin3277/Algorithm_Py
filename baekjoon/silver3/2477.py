# 참외밭
import sys
sys.stdin = open("input.txt", "r")

K = int(input())
# 동쪽은 1, 서쪽은 2, 남쪽은 3, 북쪽은 4
all_list = [] # 모든 길이 저장할 리스트
len_list = [0]*4 # 네변의 길이 저장할 리스트
small_len = [] # 작은 직사각형 길이 저장할 리스트
for _ in range(6):
    A, B = map(int, input().split())
    all_list.append(B)
    small_len.append(B)
    len_list[A-1] += B
wid_len = all_list.index(len_list[0]) # 총 가로 길이 입력받은 인덱스
hei_len = all_list.index(len_list[2]) # 총 세로 길이 입력받은 인덱스
small_len.remove(len_list[0]) # 가로 총 길이 삭제
small_len.remove(len_list[2]) # 세로 총 길이 삭제
if all_list[(wid_len+1) % 6] != len_list[2]: # 가로 총길이 다음에 세로 총길이가 나오지 않으면
    small_len.remove(all_list[(wid_len+1) % 6]) # 바로 다음 값 삭제(%6으로 인덱스 넘으면 앞으로 가도록 처리)
else: # 나오면
    small_len.remove(all_list[(wid_len+2) % 6]) # 2개 인덱스 이후의 값 삭제

if all_list[(hei_len+1) % 6] != len_list[0]: # 세로 총길이 다음에 바로 가로 총길이가 나오지 않으면
    small_len.remove(all_list[(hei_len+4) % 6]) # 바로 다음 값 삭제
else: # 나오면
    small_len.remove(all_list[(hei_len+5) % 6]) # 5개 이후의 값 삭제
res = (len_list[0]*len_list[2]) - (small_len[0]*small_len[1]) # 큰 직사각형에서 작은 직사각형 빼주기
print(res*K) # 한칸에 자라는 참외 개수 곱해주기