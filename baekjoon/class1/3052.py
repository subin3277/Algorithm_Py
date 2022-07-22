mod_list = []
for i in range(10) : 
    N = int(input())
    if not (N%42 in mod_list) :
        mod_list.append(N%42)

print(len(mod_list))