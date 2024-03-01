# 순열 장난
num = input()

# N 알아내기
if len(num) < 10 :
    N = len(num)
else :
    N = (len(num) - 9)//2 + 9

ans = []

def BT(lst, res) :
    global ans
    # 하나 출력했으면 그만
    if len(ans) > 0:
        return
    
    # 같으면 답 저장
    if len(lst) >= N :
        if res == num :
            ans = lst
        return

    # 다음 1자리 혹은 2자리 숫자 추가하기
    for i in range(1, 3) :
        n_num = num[len(res) : len(res) + i]
        # N범위에 들어오고 이미 추가하지 않은 수만
        if int(n_num[0]) != 0 and 0 < int(n_num) <= N and n_num not in lst :
            BT([*lst, n_num], res+n_num)

BT([], '')
print(*ans)