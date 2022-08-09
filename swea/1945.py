import sys
sys.stdin = open("input.txt", "r")

# 나누는 함수
def divide(N, k) :
    count = 0
    # 나눌 숫자로 나눌 수 있을 때까지
    while N % k == 0:
        count += 1
        N /= k
    # 나누고 남은 몫과 나눈 횟수 return
    return N, count

T = int(input())
for test in range(1, T+1):
    N = int(input())
    # 나누어야할 수 리스트
    num_list = [2, 3, 5, 7, 11]
    # 카운트 저장할 리스트
    count_list = [0]*5
    for i in range(5):
        res = divide(N, num_list[i])
        N = res[0]
        count_list[i] += res[1]
    print(f'#{test}', *count_list)