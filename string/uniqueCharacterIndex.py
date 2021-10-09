def firstUniqChar(s):
    if len(s) == 0:
        return -1
    seen = {}
    for i in range(len(s)):
        if s[i] in seen:
            pass
        else:
            seen[s[i]] = 1
            if s[i] not in s[i + 1:]:
                return i
    return -1
print(firstUniqChar('lovecodingonleetcode'))