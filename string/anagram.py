def anagram(s,t):
    tdic = {}
    sdic = {}
    for item in t:
        if item in tdic:
            tdic[item] += 1
        else:
            tdic[item] = 1
    for item in s:
        if item in sdic:
            sdic[item] += 1
        else:
            sdic[item] = 1
    print(tdic,sdic)
    return tdic == sdic
string1 = 'publicrelations'
string2 = 'crapbuiltonlies'
print(anagram(string1,string2))