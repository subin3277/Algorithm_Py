def getFinalString(s):
    # Write your code here
    while 'AWS' in s:
        s = s.replace('AWS', '', 1)
    if len(s) == 0:
        return -1
    else:
        return s

s = 'AAWSWS'
print(getFinalString(s))