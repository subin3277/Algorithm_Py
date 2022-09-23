# 방금그곡

def solution(m, musicinfos):
    answer = ''
    dic = {'C': 0, 'C#': 1, 'D': 2, 'D#': 3, 'E': 4, 'F': 5, 'F#': 6, 'G': 7, 'G#': 8, 'A': 9, 'A#': 10,'B': 11}

    mcode = ""
    for j in m:
        if j == "#":
            tmp = mcode[-1]
            mcode = mcode[0:len(mcode) - 1] + str(int(tmp) + 1)
        else:
            mcode += str(dic[j])
    print(mcode)
    ans = []

    for i in range(len(musicinfos)):
        st, et, title, code = map(str, musicinfos[i].split(","))
        if st[0:2] == et[0:2]:
            playtime = int(et[3:5]) - int(st[3:5])
        else:
            playtime = int(st[3:5]) + 60 - int(et[3:5])

        codedig = ""
        for j in code:
            if j == "#":
                tmp = codedig[-1]
                codedig = codedig[0:len(codedig)-1] + str(int(tmp) + 1)
            else:
                codedig += str(dic[j])
        realcode = ""
        k = 0
        for t in range(playtime):
            realcode += codedig[k]
            k += 1
            if k == len(codedig):
                k = 0
        if m in realcode:
            ans.append([title, playtime])
    if len(ans) == 0:
        answer = "(None)"
    elif len(ans) == 1:
        answer = ans[0][0]
    else:
        maxtime = 0
        for i in ans:
            if maxtime < i[1]:
                maxtime = i[1]
                answer = i[0]
    return answer

m ="CC#BCC#BCC#"
musicinfos = ["03:00,03:08,FOO,CC#B"]
print(solution(m, musicinfos))

# 해결 xxxxxxxxxxxxxxxxxxxxxxxx