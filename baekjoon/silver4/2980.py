# 도로와 신호등

N, L = map(int, input().split())
light = []
for i in range(N):
    tmp = list(map(int, input().split()))
    light.append(tmp)

light_index = 0
answer = 0
nowloaction = 0

while nowloaction < L:
    if light_index == len(light):
        answer += (L - nowloaction)
        break
    [next_light, R, G] = light[light_index]
    answer += (next_light - nowloaction)
    nowloaction += (next_light - nowloaction)
    if answer % (R + G) < R: # 빨간불. 기다려야함.
        answer += (R - (answer % (R + G)))
    light_index += 1
print(answer)