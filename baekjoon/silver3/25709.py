# 1 빼기

N = int(input())
answer = 0
while N > 0:
    if N == 1:
        answer += 1
        break

    str_N = str(N)
    if '1' in str_N:
        str_N = str_N.replace('1', '')
        if str_N == '' :
            N = 0
        else :
            N = int(str_N)
        answer += 1
    else :
        answer += ((N-1) % 10) 
        N -= ((N-1) % 10)
print(answer)

# 미해결xxxxxxxxxx