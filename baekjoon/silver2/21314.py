# 민겸수

K = input()
ans_lar = ""
ans_sma = ""
mcount = 0
for i in K:
    if i == 'M':
        mcount += 1
    else:
        tmp = 5*(10**mcount)
        ans_lar += str(tmp)

        if mcount > 0:
            tmp = 10**(mcount-1)
            ans_sma += str(tmp)
        ans_sma += '5'

        mcount = 0
if mcount != 0:
    tmp = 10**(mcount-1)
    ans_sma += str(tmp)
    ans_lar += '1'*mcount
print(ans_lar)
print(ans_sma)