N = int(input()) # 스위치 개수
tmp_list = list(map(int,input().split())) # 스위치 리스트
switch = []

for i in tmp_list :
    if i==1 :
        switch.append(True)
    else : 
        switch.append(False)
T = int(input()) # 학생수

for i in range(T) :
    gender, num = map(int,input().split()) # 성별, 받은 번호
    # 남자일 때 하는 행동
    if gender==1 :
        for j in range(1,N+1) :
            if j%num == 0 :
                switch[j-1] = not switch[j-1]
    else : #여자일 때
        j = num-1
        switch[j] = not switch[j] # 받은 숫자의 스위치 바꾸기

        k=1
        while True :
            if j-k < 0 or j+k >= N :
                break

            if switch[j-k]==switch[j+k] : # 대칭이면
                switch[j-k] = not switch[j-k]
                switch[j+k] = not switch[j+k]
                k+=1
            else :
                break

# 결과 출력
for k in range(N) :
    #20개 마다 줄 바꾸기
    if k % 20 == 0 and k!=0:
        print()

    if switch[k] :
        print("1",end="")
    else :
        print("0", end="")
    if (k+1)%20 != 0 :
        print("",end=" ")