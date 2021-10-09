def compressString(s):
    # ##1st Method
    # count=1
    # d={}
    # for item in s:
    #     if item in d:
    #         d[item] +=1
    #     else:
    #         d[item] = 1
    # l=''
    # for key,val in d.items():
    #     l+=key
    #     l+=str(val)
    # return l

    ##2nd Approach
    r=""
    length=len(s)
    if length==0:
        return ""
    if length==1:
        return s+"1"
    i=1
    count=1
    while i<length:
        if s[i]==s[i-1]:
            count+=1
        else:
            r+=s[i-1]+str(count)
            count=1
        i+=1
    r += s[i-1]+ str(count)
    return r

print(compressString('aaaabbbccd'))