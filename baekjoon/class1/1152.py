str = input()
word_list = []
word_list = str.split(' ')
count = len(word_list)
for i in word_list : 
    if i == '' :
        count -= 1

print(count)