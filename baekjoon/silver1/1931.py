# 회의실 배정
N = int(input())
time = []
for _ in range(N):
    time.append(list(map(int, input().split())))
time.sort(key=lambda x: (x[1], x[0])) # 시작시간 오름차순 정렬

cnt = 1
end_time = time[0][1] # 끝나는 시간
for i in range(1, N):
    if time[i][0] >= end_time: # 다음 시작하는 시간이 끝나는시간보다 크거나 같을 때
        cnt += 1 # 횟수 증가
        end_time = time[i][1] # 끝나는 시간 다시 설정

print(cnt)