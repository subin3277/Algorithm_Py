def longestChain(words):
    word_set = set(words) # 여기가 포인트였다...
    words.sort(key=lambda x: len(x))
    # words_list = [[] for _ in range(len(words[-1])+1)]
    # dp = {}
    # for word in words:
    #     words_list[len(word)].append(word)
    #
    # def tmp(word):
    #     if word in dp:
    #         return dp[word]
    #     max_len = 1
    #     for i in range(len(word)):
    #         new_word = word[:i] + word[i + 1:]
    #         if new_word in word_set:
    #             max_len = max(max_len, tmp(new_word) + 1)
    #     dp[word] = max_len
    #     return max_len
    #
    # max_res = 1
    # for word_gp in words_list:
    #     for word in word_gp:
    #         max_res = max(max_res, tmp(word))
    #
    # return max_res

    dp = {}

    for word in words:
        dp[word] = 1
        for i in range(len(word)):
            new_word = word[:i] + word[i+1:]
            if new_word in word_set and dp[new_word] + 1 > dp[word]:
                dp[word] = dp[new_word] + 1

    return max(dp.values())

words = ['a', 'b', 'bda', 'ba', 'bca', 'bdca']
print(longestChain(words))