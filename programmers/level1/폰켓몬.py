def solution(nums):
    answer = 0
    num = len(nums)//2
    dict = {}
    for i in nums:
        dict[i] = dict.get(i, 0) + 1
    answer = min(len(dict), num)
    return answer