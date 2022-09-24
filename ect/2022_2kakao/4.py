

cnt = 1
def solution(numbers):
    def inorder(n, num):
        global cnt
        if n <= num:
            inorder(n * 2, num)
            num_list[n] = cnt
            cnt += 1
            inorder(n * 2 + 1, num)

    answer = []
    tmp = 0
    for num in numbers:

        bit2 = bin(num)
        bit2 = bit2[2::]
        num = len(bit2)
        num_list = [0] * (num + 1)
        inorder(1, num)
        for i in range(1, len(num_list)):
            num_list[i] -= tmp
        tmp += num
        for i in range(len(bit2)):
            if bit2[i] == "0":
                num_list[num_list.index(i + 1)] = 0
        node = k =1
        while node < num:
            node += k*2
            k += 1
        k = (k-1)*2

        if 0 in num_list[1:len(num_list)-k+ 1]:
            answer.append(0)
        else:
            answer.append(1)
    return answer
numbers = [63, 111, 95]
print(solution(numbers))