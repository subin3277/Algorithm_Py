# 다트게임

dart = input()
score = []
i = 0
ten = False
for i in range(len(dart)):
    if dart[i] == 'S':
        score[-1] = score[-1] ** 1
        ten = False
    elif dart[i] == 'D':
        score[-1] = score[-1] ** 2
        ten = False
    elif dart[i] == 'T':
        score[-1] = score[-1] ** 3
        ten = False
    elif dart[i] == '*':
        if len(score) < 2:
            score[0] *= 2
        else:
            score[-1] *= 2
            score[-2] *= 2
    elif dart[i] == '#':
        score[-1] = score[-1] * (-1)
    else:
        if dart[i] == '0' and ten:
            score[-1] = 10
            ten = False
        elif dart[i] == '1':
            ten = True
            score.append(1)
        else:
            ten = False
            score.append(int(dart[i]))
print(sum(score))