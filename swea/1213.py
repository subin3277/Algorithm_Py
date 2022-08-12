# String
import sys
sys.stdin = open("input.txt", "r", encoding='UTF8')

T = 10
for test in range(1, T+1):
    test_case = int(input())
    find_str = input()
    sentence = input()
    strlen = len(find_str)
    count = 0
    for i in range(len(sentence)): # 찾을 문장 길이 동안
        state = False
        for j in range(strlen):
            if i+j < len(sentence) and sentence[i+j] == find_str[j]: # 찾아야할 문자를 찾으면 연속으로 찾기
                state = True
            else :
                 state = False
                 break
        if state: # 참이라면 count +1
            count += 1
    print(f'#{test} {count}')