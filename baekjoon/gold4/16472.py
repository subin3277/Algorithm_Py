# 고냥이

N = int(input())
speak = input()
answer = 0

i = 0
j = 1
cnt = dict()
cnt[speak[0]] = 1

while j < len(speak):
    cnt[speak[j]] = cnt.get(speak[j], 0) + 1

    while len(cnt) > N :
        cnt[speak[i]] -= 1
        if cnt[speak[i]] == 0 :
            del cnt[speak[i]]
        i += 1
    answer = max(answer, j - i + 1)
    j += 1

print(answer)