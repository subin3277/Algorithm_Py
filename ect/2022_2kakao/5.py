from collections import deque
def solution(commands):
    answer = []
    table = [["#"] * 50 for _ in range(50)]
    merge = [[[] for _ in range(50)] for _ in range(50)]
    for i in commands:
        tmp = list(map(str,i.split()))
        com = tmp[0]
        if com == "UPDATE":
            if len(tmp) == 4:
                r = int(tmp[1]) - 1
                c = int(tmp[2]) - 1
                value = tmp[3]
                table[r][c] = value
                for j in merge[r][c]:
                    table[j[0]][j[1]] = value
            else:
                value1 = tmp[1]
                value2 = tmp[2]
                for x in range(50):
                    if table[x].count(value1) >= 1:
                        for y in range(50):
                            if table[x][y] == value1:
                                table[x][y] = value2
                                for j in merge[x][y]:
                                    table[j[0]][j[1]] = value2
        elif com == "MERGE":
            r1 = int(tmp[1]) - 1
            c1 = int(tmp[2]) - 1
            r2 = int(tmp[3]) - 1
            c2 = int(tmp[4]) - 1
            tmp = [(r1, c1), (r2, c2)]
            merge[r1][c1] += merge[r2][c2] + tmp
            merge[r1][c1] = list(set(merge[r1][c1]))
            for m in merge[r1][c1]:
                merge[m[0]][m[1]] = merge[r1][c1]

            if table[r1][c1] != "#":
                for m in merge[r1][c1]:
                    table[m[0]][m[1]] = table[r1][c1]
            else:
                for m in merge[r1][c1]:
                    table[m[0]][m[1]] = table[r2][c2]
        elif com == "UNMERGE":
            r = int(tmp[1]) - 1
            c = int(tmp[2]) - 1
            for m in merge[r][c]:
                if m != (r, c):
                    table[m[0]][m[1]] = "#"
                    merge[m[0]][m[1]] = []
            merge[r][c] = []
        elif com == "PRINT":
            r = int(tmp[1]) - 1
            c = int(tmp[2]) - 1
            if table[r][c] != "#":
                answer.append(table[r][c])
            else:
                answer.append("EMPTY")
    return answer

commands = ["UPDATE 1 1 a", "UPDATE 1 2 b", "UPDATE 2 1 c", "UPDATE 2 2 d", "MERGE 1 1 1 2", "MERGE 2 2 2 1", "MERGE 2 1 1 1", "PRINT 1 1", "UNMERGE 2 2", "PRINT 1 1"]
print(solution(commands))