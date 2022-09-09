# 연산자 끼워넣기

N = int(input())
num_list = list(map(int, input().split()))
A, B, C, D = map(int, input().split())
cal = ["+"] * A + ["-"] * B + ["*"] * C + ["/"] * D

maxres = -1000000000
minres = 1000000000
if len(cal) == 1:
    if cal[0] == '+':
        maxres = minres = num_list[0] + num_list[1]
    elif cal[0] == '-':
        maxres = minres = num_list[0] - num_list[1]
    elif cal[0] == '*':
        maxres = minres = num_list[0] * num_list[1]
    elif cal[0] == '/':
        maxres = minres = num_list[0] // num_list[1]
else:

    for i in range(len(cal)):
        for j in range(len(cal)-1):
            tmp = num_list[0]
            for k in range(1, len(num_list)):
                if cal[k-1] == '+':
                    tmp += num_list[k]
                elif cal[k-1] == '-':
                    tmp -= num_list[k]
                elif cal[k-1] == '*':
                    tmp *= num_list[k]
                elif cal[k-1] == '/':
                    tmp = tmp // num_list[k]
            maxres = max(maxres, tmp)
            minres = min(minres, tmp)
            cal[j], cal[j+1] = cal[j+1], cal[j]
            print(cal)

print(maxres)
print(minres)

#해결xxxxxxxxxxx