# 암호코드 스캔_교수님 풀이
# [1] 16진수를 이진수로 바꾼다.
# [2] 카운트 배열에 변환해서 저장 cnt = [3,2,1,1,2,2,2,1,2,...,6,3,9(3배 두꺼운거)]
# cnt에서 각 min 값을 찾아서 (각 요소//min) => (6,3,9) = (2,1,3)
# [3]
# for i in range (1,len(cnt),4):
#     min = min(cnts[i:i+3])
#     key = str(cnts[i]//min) + str(cnts[i+1]//min) + str(cnts[i+2])//min)
#     pwd.append(dict3[key])
# pwd = [8, 9, ..., 8, ...] -> 8의 배수개
# [4] 8개씩 읽어서 정상코드확인 후, 정상이면 누적

import sys
sys.stdin = open("input.txt", "r")

T = int(input())
dict1 = {'0':'0001101','1' : '0011001', '2' : '0010011','3' : '0111101','4' : '0100011','5': '0110001', '6' : '0101111', '7':'0111011','8':'0110111','9':'0001011'}
dict3 = {'211':0,'221':1,'122':2,'411':3,'132':4,'231':5,'114':6,'312':7,'213':8,'112':9}
for test in range(1, T+1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]
    old = []
    ans = []
    for st in arr:
        if st != old and st.count('0')!=len(st):
            old = st # 이전 문자열과 바뀌면 처리
            bst = ""
            for ch in st:
                bst += dict1[ch]

            # [2] 0,1 갯수 저장 cnts
            old = 0
            cnts = []
            for i in range(len(bst)):
                if bst[old] != bst[i]:
                    cnts.append(i-old)
                    old = i

            # [3] 가장 작은 width을 기준으로 나눗셈(단위두께)
            pwd = []
            for i in range(1, len(cnts), 4):
                mn = cnts[i:i+3]
                key = str(cnts[i]//mn) + str(cnts[i+1]//mn + str(cnts[i+2]//mn))
                pwd.append(dict3[key])

            # [4] 8개씩 숫자 중복 제거해서 리스트 만들기

            for i in range(0, len(pwd), 8):
                if pwd[i:i+8] not in ans:
                    ans.append(pwd[i:i+8])
    sol = 0
    for code in ans:
        even = odd = 0
        for i in range(0, 8, 2):
            even += code[i] * 3
            odd += code[i+1]
        if (even * 3 + odd) % 10 == 0:
            sol += even + odd

    print(f'#{test} {sol}')
