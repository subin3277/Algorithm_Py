# 전기버스
T = int(input())
for test in range(1, T+1):
    K, N, M = map(int, input().split())
    station = list(map(int, input().split()))
    # 충전소 있는 곳 리스트
    stat_list = [False] * (N+1)
    for i in station:
        stat_list[i] = True

    i = K
    last = 0
    count = 0
    while i < N:
        # 도착한 곳에 충전소가 있다면
        if stat_list[i]:
            # 충전 횟수 증가
            count += 1
            # 마지막 충전 장소 저장
            last = i
            # 최대 갈수 있는 만큼 이동
            i += K
        # 이동한 곳에 충전소 없다면
        else:
            # 뒤로 한칸
            i -= 1
            # 마지막 충전한 곳까지 돌아갔다면 더 이동 불가하다는 뜻
            if last == i:
                count = 0
                break
    print(f'#{test} {count}')