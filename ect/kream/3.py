
def maxLength(a, k):
    start = 0
    end = 0
    current_sum = a[0]
    max_len = 0
    max_sum_subarray = []

    while end < len(a):
        if current_sum <= k:
            subarray_length = end - start + 1
            if subarray_length > max_len:
                max_len = subarray_length
                max_sum_subarray = a[start:end+1]

            end += 1
            if end < len(a):
                current_sum += a[end]
        else:
            current_sum -= a[start]
            start += 1

    return len(max_sum_subarray)

a = [1,2,3]
print(maxLength(a, 4))