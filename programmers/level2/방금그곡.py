# 방금그곡

def solution(m, musicinfos):
    answer = ''
    music = []
    codelst = []
    for i in range(len(musicinfos)):
        st, et, title, code = map(str, musicinfos[i].split(","))
        if st[0:2] == et[0:2]:
            playtime = int(et[3:5]) - int(st[3:5])
        else:
            playtime = int(st[3:5]) + 60 - int(et[3:5])
        music.append(title)
        realcode = ""
        j = k = 0
        while j < playtime:
            if k == len(code):
                k = 0
            if code[k] == "#":
                j -= 1
            realcode += code[k]
            j += 1
            k += 1
        if j == playtime and k < len(code) and code[k] == "#":
            realcode += "#"
        codelst.append(realcode)
    for i in range(len(codelst)):
        if m in codelst[i] and (m[-1] == "#" or codelst[i][codelst[i].index(m) + len(m)] != "#"):
            answer = music[i]
            break
    else:
        answer = "(None)"
    return answer

m ="ABCDEFG"
musicinfos = ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]
print(solution(m, musicinfos))

# 해결 xxxxxxxxxxxxxxxxxxxxxxxx