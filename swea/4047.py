# 영준이의 카드 카운팅
import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test in range(1, T+1):
    S = input() # SDHC
    res = ''
    card = {'S':[], 'D':[], 'H':[], 'C':[]}
    for i in range(0, len(S), 3):
        if int(S[i+1:i+3]) in card.get(S[i]):
            res = 'ERROR'
            break
        card[S[i]].append(int(S[i+1:i+3]))

    if res != 'ERROR':
        sol = []
        for i, j in card.items():
            sol.append(13 - len(j))
        print(f'#{test}', *sol)
    else:
        print(f'#{test} ERROR')
