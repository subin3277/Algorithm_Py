# 경비원
import sys
sys.stdin = open("input.txt", "r")

W, H = map(int, input().split())
N = int(input())
mar_list = []
for i in range(N):
    tmp = list(map(int, input().split()))
    mar_list.append(tmp)
A, B = map(int, input().split()) # 동근이 위치
maxres = 0
res = 0
for i in range(N):
    if mar_list[i][0] == A:
        res = abs(B - mar_list[i][1])
    elif mar_list[i][0]+A == 3:
        res = min(mar_list[i][1]+B, W*2 - mar_list[i][1] - B) + H
    elif mar_list[i][0]+A == 7:
        res = min(mar_list[i][1]+W, W*2 - mar_list[i][1] - B) + W
    else:
        if abs(A - mar_list[i][0]) == 2:
            res = B + mar_list[i][1]
            if A == 2 or A == 4:
                res += W+H
        else:
            if A == 1 or A == 2:
                res = B - mar_list[i][1]
            else:
                res = mar_list[i][1] - B

            if A == 1 or A == 4:
                res = W - res
            else :
                res = H + res

    maxres += res
print(maxres)
# 해결xxxxxxxxxxxxxxxxxxxxxxxxxxxx

