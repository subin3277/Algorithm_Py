N = int(input())

input_list = []
for i in range(N) :
    input_list.append(input())

for i in range(len(input_list[0])) :
    for j in range(1,len(input_list)) :
        
        if input_list[0][i] != input_list[j][i]:
            tmp = list(input_list[0])
            tmp[i] = '?'
            input_list[0] = "".join(tmp)
            break

res = input_list[0]
print(res)