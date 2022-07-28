N = int(input())
my_dict = [[]*N for i in range(51)]
for i in range(N) :
    word = input()
    wordlen = len(word)
    my_dict[wordlen] += [word]


for i in my_dict :
    tmp = set(i)
    i = list(tmp)
    i.sort()
    for j in i :
        print(j)
