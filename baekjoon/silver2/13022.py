# 늑대와 올바른 단어

case = ['wolf', 'wwolfolf', 'wwoollff', 'wwwooolllfff', 'wolfwwoollff', 'wolfwwoollffwolf', 'wfol', 'wwolfolf', 'wwwoolllfff' ]
# 1 0 1 1 1 1 0 0 0

N = input()

wolf = ['w', 'o', 'l', 'f']
wolf_cnt = [0, 0, 0, 0]
ans = 1

j = 0
for i in range(len(N)) :
    if N[i] == wolf[j] :
        wolf_cnt[j] += 1
        if i < len(N)-1 and N[i] == N[i+1] :
            j -= 1
        elif N[i] == 'f' and(i == len(N)-1 or N[i+1] != 'f'):
            if max(wolf_cnt) != min(wolf_cnt) :
                ans = 0
                break
            wolf_cnt = [0, 0, 0, 0]
        elif i == len(N)-1 and N[i] != 'f' :
            ans = 0
            break
        j += 1
        j = j % 4
    else :
        ans = 0
        break
print(ans)